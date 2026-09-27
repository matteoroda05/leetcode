# [0200] Number of Islands

- **Difficulty:** Medium
- **Latest accepted:** 2026-09-25 16:46 UTC
- **Resubmissions (>48 hours):** 1

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-08-15 09:18 UTC | Python3 | 213 ms (97.7%) | 21.5 MB (73.8%) | [Code](solution-v1.py) |
| v2 | 2026-09-25 16:46 UTC | Python3 | 230 ms (87.6%) | 21.5 MB (92.5%) | [Code](solution-v2.py) |

---

### Description
Given an m x n 2D binary grid grid which represents a map of &#39;1&#39;s (land) and &#39;0&#39;s (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

&nbsp;
Example 1:


Input: grid = [
  [&quot;1&quot;,&quot;1&quot;,&quot;1&quot;,&quot;1&quot;,&quot;0&quot;],
  [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;1&quot;,&quot;0&quot;],
  [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;0&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;]
]
Output: 1


Example 2:


Input: grid = [
  [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;1&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;0&quot;,&quot;0&quot;,&quot;1&quot;,&quot;0&quot;,&quot;0&quot;],
  [&quot;0&quot;,&quot;0&quot;,&quot;0&quot;,&quot;1&quot;,&quot;1&quot;]
]
Output: 3


&nbsp;
Constraints:


	m == grid.length
	n == grid[i].length
	1 &lt;= m, n &lt;= 300
	grid[i][j] is &#39;0&#39; or &#39;1&#39;.
