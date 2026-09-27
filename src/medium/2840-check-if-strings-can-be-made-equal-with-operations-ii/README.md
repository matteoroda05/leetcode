# [2840] Check if Strings Can be Made Equal With Operations II

- **Difficulty:** Medium
- **Latest accepted:** 2026-08-25 12:00 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-08-25 12:00 UTC | Python3 | 48 ms (92.1%) | 20.1 MB (78.7%) | [Code](solution-v1.py) |

---

### Description
You are given two strings s1 and s2, both of length n, consisting of lowercase English letters.

You can apply the following operation on any of the two strings any number of times:


	Choose any two indices i and j such that i &lt; j and the difference j - i is even, then swap the two characters at those indices in the string.


Return true if you can make the strings s1 and s2 equal, and&nbsp;false otherwise.

&nbsp;
Example 1:


Input: s1 = &quot;abcdba&quot;, s2 = &quot;cabdab&quot;
Output: true
Explanation: We can apply the following operations on s1:
- Choose the indices i = 0, j = 2. The resulting string is s1 = &quot;cbadba&quot;.
- Choose the indices i = 2, j = 4. The resulting string is s1 = &quot;cbbdaa&quot;.
- Choose the indices i = 1, j = 5. The resulting string is s1 = &quot;cabdab&quot; = s2.


Example 2:


Input: s1 = &quot;abe&quot;, s2 = &quot;bea&quot;
Output: false
Explanation: It is not possible to make the two strings equal.


&nbsp;
Constraints:


	n == s1.length == s2.length
	1 &lt;= n &lt;= 105
	s1 and s2 consist only of lowercase English letters.
