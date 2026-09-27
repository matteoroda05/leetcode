import os
import re
import json
import time
import subprocess
import requests
from datetime import datetime, timezone
from collections import Counter
from collections import defaultdict
import urllib.parse
from pathlib import Path

LEETCODE_SESSION = os.environ.get("LEETCODE_SESSION")
CSRF_TOKEN = os.environ.get("LEETCODE_CSRF_TOKEN")
VERSION_WINDOW_SECONDS = 48 * 60 * 60
REFRESH_UNCHANGED = os.environ.get("REFRESH_UNCHANGED", "false").lower() in ("true", "1", "yes")

GRAPHQL_URL = "https://leetcode.com/graphql"
HEADERS = {
    "Cookie": f"csrftoken={CSRF_TOKEN}; LEETCODE_SESSION={LEETCODE_SESSION};",
    "Referer": "https://leetcode.com",
    "Content-Type": "application/json",
    "x-csrftoken": CSRF_TOKEN or ""
}

EXTENSIONS = {
    "python": "py", "python3": "py", "cpp": "cpp", "c": "c",
    "java": "java", "javascript": "js", "typescript": "ts",
    "golang": "go", "csharp": "cs", "ruby": "rb", "swift": "swift",
    "rust": "rs", "kotlin": "kt", "scala": "scala", "php": "php"
}

LANG_DISPLAY = {
    "python": "Python", "python3": "Python3", "cpp": "C++", "c": "C",
    "java": "Java", "javascript": "JavaScript", "typescript": "TypeScript",
    "golang": "Go", "csharp": "C#", "ruby": "Ruby", "swift": "Swift",
    "rust": "Rust", "kotlin": "Kotlin"
}

def gql_request(query, variables=None):
    res = requests.post(
        GRAPHQL_URL,
        headers=HEADERS,
        json={"query": query, "variables": variables or {}},
        timeout=30,
    )
    if res.status_code != 200:
        raise RuntimeError(f"LeetCode API returned HTTP {res.status_code}")
    payload = res.json()
    if payload.get("errors"):
        raise RuntimeError(f"LeetCode API reported an error: {payload['errors']}")
    return payload.get("data", {})

def get_submission_list():
    query = """
    query getSubmissions($offset: Int!,$limit: Int!) {
        submissionList(offset: $offset, limit:$limit) {
            submissions {
                id
                statusDisplay
                lang
                runtime
                timestamp
                title
                titleSlug
                memory
            }
            hasNext
        }
    }
    """
    submissions = []
    offset = 0
    limit = 20
    while True:
        data = gql_request(query, {"offset": offset, "limit": limit})
        if not data or not data.get("submissionList"):
            raise RuntimeError(f"Could not load submissions page at offset {offset}")
        sub_list = data["submissionList"]
        for sub in sub_list.get("submissions", []):
            if sub.get("statusDisplay") == "Accepted":
                submissions.append(sub)
        if not sub_list.get("hasNext"):
            break
        offset += limit
        time.sleep(0.4)
    return submissions

def get_submission_details(submission_id):
    query = """
    query submissionDetails($submissionId: Int!) {
        submissionDetails(submissionId: $submissionId) {
            code
            runtime
            runtimeDisplay
            runtimePercentile
            memory
            memoryDisplay
            memoryPercentile
            question {
                questionFrontendId
                title
                titleSlug
                difficulty
                content
            }
        }
    }
    """
    data = gql_request(query, {"submissionId": int(submission_id)})
    if data and "submissionDetails" in data:
        return data["submissionDetails"]
    return None

def group_versions(submissions):
    """One version per 48-hour window, retaining its latest accepted submission.

    The window begins with the first accepted submission in that version. A
    submission more than 48 hours after the window began starts the next version. Sorting explicitly
    avoids relying on LeetCode's API response order.
    """
    by_problem = defaultdict(list)
    for submission in submissions:
        by_problem[submission["titleSlug"]].append(submission)

    grouped = {}
    for slug, history in by_problem.items():
        history.sort(key=lambda s: (int(s["timestamp"]), int(s["id"])))
        versions = []
        for submission in history:
            timestamp = int(submission["timestamp"])
            if not versions or timestamp - versions[-1]["started_at"] > VERSION_WINDOW_SECONDS:
                versions.append({"started_at": timestamp, "submission": submission})
            else:
                versions[-1]["submission"] = submission
        grouped[slug] = versions
    return grouped

def update_readme(problems_data):
    stats = {"easy": 0, "medium": 0, "hard": 0}
    lang_counter = Counter()

    for p in problems_data:
        diff = p["difficulty"].lower()
        if diff in stats:
            stats[diff] += 1
        
        lang_display_name = LANG_DISPLAY.get(p["lang"], p["lang"].capitalize())
        lang_counter[lang_display_name] += 1

    total = stats["easy"] + stats["medium"] + stats["hard"]

    if lang_counter:
        labels = list(lang_counter.keys())
        data_values = list(lang_counter.values())
        chart_config = {
            "type": "doughnut",
            "data": {
                "labels": labels,
                "datasets": [{
                    "data": data_values,
                    "backgroundColor": [
                        "#3572A5", "#F1E05A", "#4F5D95", "#00ADD8", 
                        "#DEA584", "#B07219", "#E34C26", "#563D7C"
                    ][:len(labels)]
                }]
            },
            "options": {
                "plugins": {
                    "legend": {"position": "bottom", "labels": {"fontColor": "#ffffff", "fontSize": 12}},
                    "doughnutlabel": {
                        "labels": [{"text": str(total), "font": {"size": 20}}, {"text": "Solved"}]
                    }
                }
            }
        }
        encoded_chart = urllib.parse.quote(json.dumps(chart_config))
        chart_url = f"https://quickchart.io/chart?c={encoded_chart}&w=300&h=260&bkg=%2318181b"
        chart_img_md = f'<img src="{chart_url}" alt="Language Breakdown" width="280" />'
    else:
        chart_img_md = "*No submissions indexed yet.*"

    lang_badges = " ".join([
        f'`{lang}: {count} ({round((count / total) * 100, 1)}%)`'
        for lang, count in lang_counter.most_common()
    ]) if total > 0 else "N/A"

    table_rows = []
    for p in sorted(problems_data, key=lambda x: int(x["qid"])):
        qid = p["qid"]
        title = p["title"]
        slug = p["slug"]
        diff = p["difficulty"]
        diff_tag = (
            f"`Easy`" if diff == "Easy" else
            f"`Medium`" if diff == "Medium" else
            f"`Hard`"
        )
        lc_url = f"https://leetcode.com/problems/{slug}/"
        solution_rel_url = p["versions"][-1]["path"]
        lang_name = LANG_DISPLAY.get(p["lang"], p["lang"])

        table_rows.append(
            f"| {qid} | [{title}]({lc_url}) | [v{len(p['versions'])}]({solution_rel_url}) | {lang_name} | {diff_tag} | {p['runtime']} ({p['runtime_pct']}) | {p['memory']} ({p['memory_pct']}) | {p['date']} | {p['resubmissions']} |"
        )

    rows_str = "\n".join(table_rows)
    repeated = sum(p["resubmissions"] > 0 for p in problems_data)

    readme_content = f"""<div align="center">

# 💻 LeetCode Solutions & Analytics

[![Website](https://img.shields.io/badge/Website-matteoroda.com%2Fleetcode-4F46E5?style=for-the-badge&logo=googlechrome&logoColor=white)](https://matteoroda.com/leetcode/)
[![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=LeetCode&logoColor=black)](https://leetcode.com/u/Matteoroda/)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white)](https://github.com/matteoroda05)

Automated archive tracking algorithm practice, solutions, and benchmarks.

---

## 📊 LeetCode Stats

<div align="center">

[![LeetCode Stats](https://leetcard.jacoblin.cool/Matteoroda?theme=dark&font=Nunito&ext=heatmap)](https://leetcode.com/u/Matteoroda/)

</div>

---

## 🛠️ Languages Used

<div align="center">

{chart_img_md}

<br/>

{lang_badges}

</div>

---

### 📈 Local Progress Breakdown

| 🟢 Easy | 🟡 Medium | 🔴 Hard | 🏆 Total Solved |
| :---: | :---: | :---: | :---: |
| **{stats['easy']}** | **{stats['medium']}** | **{stats['hard']}** | **{total}** |

**{repeated} problems revisited more than 48 hours later.** A resubmission is a new
48-hour version window; submissions within the same window update that version.

---

</div>

### 📑 Index of Solutions

| # | Title | Solution | Language | Difficulty | Runtime | Memory | Date Solved | Resubmission |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
{rows_str}

---

<div align="center">
<sub>Automatically synced and updated via custom GitHub Actions engine.</sub>
</div>
"""
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

def update_site_data(problems_data):
    os.makedirs("docs", exist_ok=True)
    with open("docs/data.json", "w", encoding="utf-8") as f:
        json.dump({"profile": "Matteoroda", "problems": problems_data}, f, ensure_ascii=False, indent=2)
        f.write("\n")

def previous_records():
    if not os.path.exists("docs/data.json"):
        return {}
    with open("docs/data.json", encoding="utf-8") as f:
        data = json.load(f)
    return {problem["slug"]: problem for problem in data.get("problems", [])}


def has_same_versions(windows, previous):
    if not previous or len(previous.get("versions", [])) != len(windows):
        return False
    return all(str(old["submission_id"]) == str(window["submission"]["id"])
               for old, window in zip(previous["versions"], windows))


def saved_files_exist(previous):
    folder = os.path.dirname(previous["versions"][-1]["path"])
    return (os.path.exists(os.path.join(folder, "README.md")) and
            all(os.path.exists(v["path"]) for v in previous["versions"]))


def save_problem(record, question, code_by_path, previous=None):
    target_dir = os.path.join("src", record["difficulty"].lower(),
                              f"{record['qid']}-{record['slug']}")
    os.makedirs(target_dir, exist_ok=True)
    old_versions = {v["version"]: v for v in (previous or {}).get("versions", [])}
    for version in record["versions"]:
        path = version["path"]
        old = old_versions.get(version["version"])
        if (not REFRESH_UNCHANGED and old and os.path.exists(path) and
                old["submission_id"] == version["submission_id"] and
                old["path"] == path):
            continue
        code = code_by_path[path]
        # Version files are generated from the latest accepted submission in
        # their 48-hour window. Older unversioned solution files are retained.
        if not Path(path).exists() or Path(path).read_text(encoding="utf-8") != code:
            with open(path, "w", encoding="utf-8") as f:
                f.write(code)

    readme_path = os.path.join(target_dir, "README.md")
    previous = ""
    if os.path.exists(readme_path):
        with open(readme_path, encoding="utf-8") as f:
            previous = f.read()
    # Keep the existing problem definition if there is one. The generated
    # submission history above it is refreshed on every sync.
    match = re.search(r"(?m)^### Description\s*$", previous)
    if match:
        description = previous[match.start():].strip()
    else:
        clean_html = re.sub(r"<[^>]+>", "", question.get("content", "") or "")
        description = "### Description\n" + clean_html.strip()

    rows = []
    for version in record["versions"]:
        language = LANG_DISPLAY.get(version["lang"], version["lang"])
        filename = os.path.basename(version["path"])
        rows.append(
            f"| v{version['version']} | {version['date']} | {language} | "
            f"{version['runtime']} ({version['runtime_pct']}) | "
            f"{version['memory']} ({version['memory_pct']}) | "
            f"[Code]({filename}) |"
        )
    history = "\n".join(rows)
    content = f"""# [{record['qid']}] {record['title']}

- **Difficulty:** {record['difficulty']}
- **Latest accepted:** {record['date']}
- **Resubmissions (>48 hours):** {record['resubmissions']}

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
{history}

---

{description}
"""
    if content != previous:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(content)


def main():
    subprocess.run(["git", "config", "user.name", "github-actions[bot]"], check=True)
    subprocess.run(["git", "config", "user.email", "github-actions[bot]@users.noreply.github.com"], check=True)

    grouped = group_versions(get_submission_list())
    if not grouped:
        raise RuntimeError("No accepted submissions returned; refusing to replace archive data")
    previous_by_slug = previous_records()
    problems_metadata = []
    for slug, windows in grouped.items():
        previous = previous_by_slug.get(slug)
        if (not REFRESH_UNCHANGED and has_same_versions(windows, previous) and
                saved_files_exist(previous)):
            problems_metadata.append(previous)
            continue
        versions = []
        code_by_path = {}
        question = None
        for number, window in enumerate(windows, start=1):
            sub = window["submission"]
            details = get_submission_details(sub["id"])
            if not details or not details.get("question") or details.get("code") is None:
                raise RuntimeError(f"Could not load submission {sub['id']} for {slug}")
            question = details["question"]
            qid = str(question["questionFrontendId"]).zfill(4)
            difficulty = question["difficulty"].capitalize()
            lang = sub["lang"]
            ext = EXTENSIONS.get(lang, "txt")
            timestamp = int(sub["timestamp"])
            date = datetime.fromtimestamp(timestamp, timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
            path = f"src/{difficulty.lower()}/{qid}-{slug}/solution-v{number}.{ext}"
            runtime = details.get("runtimeDisplay") or f"{details.get('runtime', 0)}ms"
            memory = details.get("memoryDisplay") or f"{round((details.get('memory') or 0) / (1024*1024), 1)}MB"
            version = {
                "version": number, "submission_id": str(sub["id"]),
                "timestamp": timestamp, "date": date, "lang": lang, "ext": ext,
                "runtime": runtime,
                "runtime_pct": f"{round(details.get('runtimePercentile') or 0, 1)}%",
                "memory": memory,
                "memory_pct": f"{round(details.get('memoryPercentile') or 0, 1)}%",
                "path": path,
            }
            versions.append(version)
            code_by_path[path] = details["code"]

        latest = versions[-1]
        record = {
            "qid": qid, "title": question["title"], "slug": slug,
            "difficulty": difficulty, "resubmissions": len(versions) - 1,
            "versions": versions,
            **{key: latest[key] for key in (
                "lang", "ext", "runtime", "runtime_pct", "memory",
                "memory_pct", "date", "timestamp")},
        }
        save_problem(record, question, code_by_path, previous)
        problems_metadata.append(record)
        time.sleep(0.3)

    problems_metadata.sort(key=lambda p: int(p["qid"]))
    update_readme(problems_metadata)
    update_site_data(problems_metadata)
    subprocess.run(["git", "add", "--", "src", "README.md", "docs/data.json"], check=True)
    if subprocess.run(["git", "diff", "--cached", "--quiet"]).returncode:
        subprocess.run(["git", "commit", "-m", "sync: archive accepted submission versions [skip ci]"], check=True)

if __name__ == "__main__":
    main()
