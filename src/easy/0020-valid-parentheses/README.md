# [0020] Valid Parentheses

- **Difficulty:** Easy
- **Latest accepted:** 2026-09-25 21:40 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-09-25 21:40 UTC | Python3 | 0 ms (100.0%) | 19.3 MB (24.8%) | [Code](solution-v1.py) |

---

### Description
Given a string s containing just the characters &#39;(&#39;, &#39;)&#39;, &#39;{&#39;, &#39;}&#39;, &#39;[&#39; and &#39;]&#39;, determine if the input string is valid.

An input string is valid if:


	Open brackets must be closed by the same type of brackets.
	Open brackets must be closed in the correct order.
	Every close bracket has a corresponding open bracket of the same type.


&nbsp;
Example 1:


Input: s = &quot;()&quot;

Output: true


Example 2:


Input: s = &quot;()[]{}&quot;

Output: true


Example 3:


Input: s = &quot;(]&quot;

Output: false


Example 4:


Input: s = &quot;([])&quot;

Output: true


Example 5:


Input: s = &quot;([)]&quot;

Output: false


&nbsp;
Constraints:


	1 &lt;= s.length &lt;= 104
	s consists of parentheses only &#39;()[]{}&#39;.
