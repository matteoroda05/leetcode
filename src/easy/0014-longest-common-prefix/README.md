# [0014] Longest Common Prefix

- **Difficulty:** Easy
- **Latest accepted:** 2026-10-11 20:53 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-10-11 20:53 UTC | Python3 | 1 ms (30.0%) | 19.4 MB (33.1%) | [Code](solution-v1.py) |

---

### Description
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string &quot;&quot;.

&nbsp;
Example 1:


Input: strs = [&quot;flower&quot;,&quot;flow&quot;,&quot;flight&quot;]
Output: &quot;fl&quot;


Example 2:


Input: strs = [&quot;dog&quot;,&quot;racecar&quot;,&quot;car&quot;]
Output: &quot;&quot;
Explanation: There is no common prefix among the input strings.


&nbsp;
Constraints:


	1 &lt;= strs.length &lt;= 200
	0 &lt;= strs[i].length &lt;= 200
	strs[i] consists of only lowercase English letters if it is non-empty.
