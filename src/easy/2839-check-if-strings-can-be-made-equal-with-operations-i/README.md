# [2839] Check if Strings Can be Made Equal With Operations I

- **Difficulty:** Easy
- **Latest accepted:** 2026-08-25 11:31 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-08-25 11:31 UTC | Python3 | 0 ms (100.0%) | 19.2 MB (90.9%) | [Code](solution-v1.py) |

---

### Description
You are given two strings s1 and s2, both of length 4, consisting of lowercase English letters.

You can apply the following operation on any of the two strings any number of times:


	Choose any two indices i and j such that j - i = 2, then swap the two characters at those indices in the string.


Return true if you can make the strings s1 and s2 equal, and false otherwise.

&nbsp;
Example 1:


Input: s1 = &quot;abcd&quot;, s2 = &quot;cdab&quot;
Output: true
Explanation: We can do the following operations on s1:
- Choose the indices i = 0, j = 2. The resulting string is s1 = &quot;cbad&quot;.
- Choose the indices i = 1, j = 3. The resulting string is s1 = &quot;cdab&quot; = s2.


Example 2:


Input: s1 = &quot;abcd&quot;, s2 = &quot;dacb&quot;
Output: false
Explanation: It is not possible to make the two strings equal.


&nbsp;
Constraints:


	s1.length == s2.length == 4
	s1 and s2 consist only of lowercase English letters.
