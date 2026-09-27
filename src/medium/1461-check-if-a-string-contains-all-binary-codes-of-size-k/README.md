# [1461] Check If a String Contains All Binary Codes of Size K

- **Difficulty:** Medium
- **Latest accepted:** 2026-02-23 12:44 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-02-23 12:44 UTC | Python | 229 ms (94.6%) | 63.2 MB (67.9%) | [Code](solution-v1.py) |

---

### Description
Given a binary string s and an integer k, return true if every binary code of length k is a substring of s. Otherwise, return false.

&nbsp;
Example 1:


Input: s = &quot;00110110&quot;, k = 2
Output: true
Explanation: The binary codes of length 2 are &quot;00&quot;, &quot;01&quot;, &quot;10&quot; and &quot;11&quot;. They can be all found as substrings at indices 0, 1, 3 and 2 respectively.


Example 2:


Input: s = &quot;0110&quot;, k = 1
Output: true
Explanation: The binary codes of length 1 are &quot;0&quot; and &quot;1&quot;, it is clear that both exist as a substring. 


Example 3:


Input: s = &quot;0110&quot;, k = 2
Output: false
Explanation: The binary code &quot;00&quot; is of length 2 and does not exist in the array.


&nbsp;
Constraints:


	1 &lt;= s.length &lt;= 5 * 105
	s[i] is either &#39;0&#39; or &#39;1&#39;.
	1 &lt;= k &lt;= 20
