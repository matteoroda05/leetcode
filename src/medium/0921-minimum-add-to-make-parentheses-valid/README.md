# [0921] Minimum Add to Make Parentheses Valid

- **Difficulty:** Medium
- **Latest accepted:** 2026-10-06 07:15 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-10-06 07:15 UTC | Python3 | 0 ms (100.0%) | 19.3 MB (49.5%) | [Code](solution-v1.py) |

---

### Description
A parentheses string is valid if and only if:


	It is the empty string,
	It can be written as AB (A concatenated with B), where A and B are valid strings, or
	It can be written as (A), where A is a valid string.


You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.


	For example, if s = &quot;()))&quot;, you can insert an opening parenthesis to be &quot;(()))&quot; or a closing parenthesis to be &quot;())))&quot;.


Return the minimum number of moves required to make s valid.

&nbsp;
Example 1:


Input: s = &quot;())&quot;
Output: 1


Example 2:


Input: s = &quot;(((&quot;
Output: 3


&nbsp;
Constraints:


	1 &lt;= s.length &lt;= 1000
	s[i] is either &#39;(&#39; or &#39;)&#39;.
