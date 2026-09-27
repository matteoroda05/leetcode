import importlib.util
import sys
import types
import unittest
import tempfile
import os
from pathlib import Path


# Grouping needs no network; the workflow installs requests for the real sync.
sys.modules.setdefault("requests", types.ModuleType("requests"))
spec = importlib.util.spec_from_file_location(
    "sync", Path(__file__).resolve().parents[1] / "scripts" / "sync.py"
)
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)


class VersionGroupingTests(unittest.TestCase):
    def test_newest_wins_within_window_and_only_over_48_hours_starts_version(self):
        start = 1_700_000_000
        submissions = [
            {"titleSlug": "two-sum", "id": str(number), "timestamp": str(start + offset)}
            for number, offset in [
                (5, 48 * 3600 + 1),
                (2, 1800),
                (4, 48 * 3600),
                (1, 0),
                (3, 47 * 3600),
            ]
        ]
        groups = sync.group_versions(submissions)["two-sum"]
        self.assertEqual([g["submission"]["id"] for g in groups], ["4", "5"])
        self.assertEqual([g["started_at"] for g in groups], [start, start + 48 * 3600 + 1])

    def test_problems_are_grouped_independently(self):
        submissions = [
            {"titleSlug": slug, "id": str(i), "timestamp": str(ts)}
            for i, (slug, ts) in enumerate([
                ("a", 100), ("b", 100), ("a", 101 + 48 * 3600),
                ("b", 130),
            ], start=1)
        ]
        groups = sync.group_versions(submissions)
        self.assertEqual(len(groups["a"]), 2)
        self.assertEqual(len(groups["b"]), 1)

    def test_unchanged_problem_can_be_preserved_or_refreshed(self):
        with tempfile.TemporaryDirectory() as temp:
            original_dir = os.getcwd()
            try:
                os.chdir(temp)
                path = "src/easy/0001-two-sum/solution-v1.py"
                version = {
                    "version": 1, "submission_id": "101", "path": path,
                    "date": "2026-09-27 12:00 UTC", "lang": "python3",
                    "runtime": "1 ms", "runtime_pct": "90%",
                    "memory": "20 MB", "memory_pct": "80%",
                }
                record = {
                    "qid": "0001", "title": "Two Sum", "slug": "two-sum",
                    "difficulty": "Easy", "date": version["date"],
                    "resubmissions": 0, "versions": [version],
                }
                question = {"content": "<p>Find two values</p>"}
                sync.save_problem(record, question, {path: "generated"})
                Path(path).write_text("hand edited")
                sync.REFRESH_UNCHANGED = False
                sync.save_problem(record, question, {path: "generated"}, record)
                self.assertEqual(Path(path).read_text(), "hand edited")
                sync.REFRESH_UNCHANGED = True
                sync.save_problem(record, question, {path: "generated"}, record)
                self.assertEqual(Path(path).read_text(), "generated")
                windows = [{"submission": {"id": "101"}}]
                self.assertTrue(sync.has_same_versions(windows, record))
                self.assertFalse(sync.has_same_versions([{"submission": {"id": "102"}}], record))
            finally:
                sync.REFRESH_UNCHANGED = False
                os.chdir(original_dir)


if __name__ == "__main__":
    unittest.main()
