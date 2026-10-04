# [0678] Valid Parenthesis String

- **Difficulty:** Medium
- **Latest accepted:** 2026-10-04 21:02 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-10-04 21:02 UTC | Python3 | 0 ms (100.0%) | 19.1 MB (90.0%) | [Code](solution-v1.py) |

---

### Description
Given a string s containing only three types of characters: &#39;(&#39;, &#39;)&#39; and &#39;*&#39;, return true if s is valid.

The following rules define a valid string:


	Any left parenthesis &#39;(&#39; must have a corresponding right parenthesis &#39;)&#39;.
	Any right parenthesis &#39;)&#39; must have a corresponding left parenthesis &#39;(&#39;.
	Left parenthesis &#39;(&#39; must go before the corresponding right parenthesis &#39;)&#39;.
	&#39;*&#39; could be treated as a single right parenthesis &#39;)&#39; or a single left parenthesis &#39;(&#39; or an empty string &quot;&quot;.


&nbsp;
Example 1:


Input: s = &quot;()&quot;
Output: true


Example 2:


Input: s = &quot;(*)&quot;
Output: true


Example 3:


Input: s = &quot;(*))&quot;
Output: true


Example 4:


Input: s = &quot;(&quot;
Output: false


&nbsp;
Constraints:


	1 &lt;= s.length &lt;= 100
	s[i] is &#39;(&#39;, &#39;)&#39; or &#39;*&#39;.
