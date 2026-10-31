# [0399] Evaluate Division

- **Difficulty:** Medium
- **Latest accepted:** 2026-10-30 17:58 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-10-30 17:58 UTC | Python3 | 0 ms (100.0%) | 19.3 MB (88.1%) | [Code](solution-v1.py) |

---

### Description
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note:&nbsp;The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.

&nbsp;
Example 1:


Input: equations = [[&quot;a&quot;,&quot;b&quot;],[&quot;b&quot;,&quot;c&quot;]], values = [2.0,3.0], queries = [[&quot;a&quot;,&quot;c&quot;],[&quot;b&quot;,&quot;a&quot;],[&quot;a&quot;,&quot;e&quot;],[&quot;a&quot;,&quot;a&quot;],[&quot;x&quot;,&quot;x&quot;]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? 
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
note: x is undefined =&gt; -1.0

Example 2:


Input: equations = [[&quot;a&quot;,&quot;b&quot;],[&quot;b&quot;,&quot;c&quot;],[&quot;bc&quot;,&quot;cd&quot;]], values = [1.5,2.5,5.0], queries = [[&quot;a&quot;,&quot;c&quot;],[&quot;c&quot;,&quot;b&quot;],[&quot;bc&quot;,&quot;cd&quot;],[&quot;cd&quot;,&quot;bc&quot;]]
Output: [3.75000,0.40000,5.00000,0.20000]


Example 3:


Input: equations = [[&quot;a&quot;,&quot;b&quot;]], values = [0.5], queries = [[&quot;a&quot;,&quot;b&quot;],[&quot;b&quot;,&quot;a&quot;],[&quot;a&quot;,&quot;c&quot;],[&quot;x&quot;,&quot;y&quot;]]
Output: [0.50000,2.00000,-1.00000,-1.00000]


&nbsp;
Constraints:


	1 &lt;= equations.length &lt;= 20
	equations[i].length == 2
	1 &lt;= Ai.length, Bi.length &lt;= 5
	values.length == equations.length
	0.0 &lt; values[i] &lt;= 20.0
	1 &lt;= queries.length &lt;= 20
	queries[i].length == 2
	1 &lt;= Cj.length, Dj.length &lt;= 5
	Ai, Bi, Cj, Dj consist of lower case English letters and digits.
