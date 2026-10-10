# [0856] Score of Parentheses

- **Difficulty:** Medium
- **Latest accepted:** 2026-10-05 21:03 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-10-05 21:03 UTC | Python3 | 0 ms (100.0%) | 19.2 MB (84.4%) | [Code](solution-v1.py) |

---

### Description
Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:


	&quot;()&quot; has score 1.
	AB has score A + B, where A and B are balanced parentheses strings.
	(A) has score 2 * A, where A is a balanced parentheses string.


&nbsp;
Example 1:


Input: s = &quot;()&quot;
Output: 1


Example 2:


Input: s = &quot;(())&quot;
Output: 2


Example 3:


Input: s = &quot;()()&quot;
Output: 2


&nbsp;
Constraints:


	2 &lt;= s.length &lt;= 50
	s consists of only &#39;(&#39; and &#39;)&#39;.
	s is a balanced parentheses string.
