import os
import re
import json
import time
import subprocess
import requests
from datetime import datetime
from collections import Counter
import urllib.parse

LEETCODE_SESSION = os.environ.get("LEETCODE_SESSION")
CSRF_TOKEN = os.environ.get("LEETCODE_CSRF_TOKEN")
OVERWRITE = os.environ.get("OVERWRITE_EXISTING", "false").lower() in ("true", "1", "yes")

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
        json={"query": query, "variables": variables or {}}
    )
    if res.status_code != 200:
        return None
    return res.json().get("data", {})

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
        if not data or "submissionList" not in data:
            break
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
        solution_rel_url = f"src/{diff.lower()}/{qid}-{slug}/solution.{p['ext']}"
        lang_name = LANG_DISPLAY.get(p["lang"], p["lang"])

        table_rows.append(
            f"| {qid} | [{title}]({lc_url}) | [Solution]({solution_rel_url}) | {lang_name} | {diff_tag} | {p['runtime']} ({p['runtime_pct']}) | {p['memory']} ({p['memory_pct']}) | {p['date']} |"
        )

    rows_str = "\n".join(table_rows)

    readme_content = f"""<div align="center">

# 💻 LeetCode Solutions & Analytics

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

---

</div>

### 📑 Index of Solutions

| # | Title | Solution | Language | Difficulty | Runtime | Memory | Date Solved |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
{rows_str}

---

<div align="center">
<sub>Automatically synced and updated via custom GitHub Actions engine.</sub>
</div>
"""
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)

def update_site_data(problems_data):
    os.makedirs("docs/leetcode", exist_ok=True)
    with open("docs/leetcode/data.json", "w", encoding="utf-8") as f:
        json.dump({"profile": "Matteoroda", "problems": problems_data}, f, ensure_ascii=False, indent=2)
        f.write("\n")

def main():
    subprocess.run(["git", "config", "user.name", "github-actions[bot]"], check=True)
    subprocess.run(["git", "config", "user.email", "github-actions[bot]@users.noreply.github.com"], check=True)

    subs = get_submission_list()
    unique_subs = {}
    for s in subs:
        slug = s["titleSlug"]
        if slug not in unique_subs:
            unique_subs[slug] = s

    ordered_subs = sorted(unique_subs.values(), key=lambda x: int(x["timestamp"]))
    problems_metadata = []

    for sub in ordered_subs:
        details = get_submission_details(sub["id"])
        if not details:
            continue

        q = details["question"]
        qid = q["questionFrontendId"].zfill(4)
        title = q["title"]
        slug = q["titleSlug"]
        difficulty = q["difficulty"].capitalize()
        diff_lower = difficulty.lower()
        code = details["code"]
        lang = sub["lang"]
        ext = EXTENSIONS.get(lang, "txt")

        sub_time = int(sub["timestamp"])
        formatted_date = datetime.fromtimestamp(sub_time).strftime("%Y-%m-%d")

        r_disp = details.get("runtimeDisplay") or f"{details.get('runtime', 0)}ms"
        r_pct = f"{round(details.get('runtimePercentile') or 0, 1)}%"
        m_disp = details.get("memoryDisplay") or f"{round((details.get('memory') or 0) / (1024*1024), 1)}MB"
        m_pct = f"{round(details.get('memoryPercentile') or 0, 1)}%"

        problems_metadata.append({
            "qid": qid,
            "title": title,
            "slug": slug,
            "difficulty": difficulty,
            "lang": lang,
            "ext": ext,
            "runtime": r_disp,
            "runtime_pct": r_pct,
            "memory": m_disp,
            "memory_pct": m_pct,
            "date": formatted_date
        })

        folder_name = f"{qid}-{slug}"
        target_dir = os.path.join("src", diff_lower, folder_name)
        os.makedirs(target_dir, exist_ok=True)

        solution_path = os.path.join(target_dir, f"solution.{ext}")
        problem_desc_path = os.path.join(target_dir, "README.md")

        # Process if file does not exist, or if OVERWRITE toggle is enabled
        if not os.path.exists(solution_path) or OVERWRITE:
            with open(solution_path, "w", encoding="utf-8") as f:
                f.write(code)

            clean_html = re.sub(r'<[^>]+>', '', q.get("content", "") or "")
            problem_readme = f"""# [{qid}] {title}

**Difficulty:** {difficulty}  
**Date Solved:** {formatted_date}  
**Runtime:** {r_disp} ({r_pct})  
**Memory:** {m_disp} ({m_pct})  

---

### Description
{clean_html.strip()}
"""
            with open(problem_desc_path, "w", encoding="utf-8") as f:
                f.write(problem_readme)

            subprocess.run(["git", "add", target_dir], check=True)
            diff_check = subprocess.run(["git", "diff", "--cached", "--quiet"]).returncode
            if diff_check != 0:
                commit_msg = f"LeetCode Sync: {qid} | {title} | {formatted_date} | Time: {r_disp} ({r_pct}) | Memory: {m_disp} ({m_pct})"
                subprocess.run(["git", "commit", "-m", commit_msg], check=True)
                time.sleep(0.3)

    update_readme(problems_metadata)
    update_site_data(problems_metadata)
    diff = subprocess.run(["git", "diff", "--quiet", "README.md"]).returncode
    if diff != 0:
        subprocess.run(["git", "add", "README.md"], check=True)
        subprocess.run(["git", "commit", "-m", "docs: update solutions index table [skip ci]"], check=True)

    if subprocess.run(["git", "status", "--porcelain", "--", "docs/leetcode/data.json"], capture_output=True, text=True, check=True).stdout:
        subprocess.run(["git", "add", "docs/leetcode/data.json"], check=True)
        subprocess.run(["git", "commit", "-m", "docs: update website data [skip ci]"], check=True)

if __name__ == "__main__":
    main()
