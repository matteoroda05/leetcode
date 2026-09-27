# [0003] Longest Substring Without Repeating Characters

- **Difficulty:** Medium
- **Latest accepted:** 2026-08-15 14:05 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-08-15 14:05 UTC | Python3 | 155 ms (95.9%) | 20 MB (37.0%) | [Code](solution-v1.py) |

---

### Description
Given a string s, find the length of the longest substring without duplicate characters.

&nbsp;
Example 1:


Input: s = &quot;abcabcbb&quot;
Output: 3
Explanation: The answer is &quot;abc&quot;, with the length of 3. Note that &quot;bca&quot; and &quot;cab&quot; are also correct answers.


Example 2:


Input: s = &quot;bbbbb&quot;
Output: 1
Explanation: The answer is &quot;b&quot;, with the length of 1.


Example 3:


Input: s = &quot;pwwkew&quot;
Output: 3
Explanation: The answer is &quot;wke&quot;, with the length of 3.
Notice that the answer must be a substring, &quot;pwke&quot; is a subsequence and not a substring.


&nbsp;
Constraints:


	0 &lt;= s.length &lt;= 105
	s consists of English letters, digits, symbols and spaces.
