# [0069] Sqrt(x)

- **Difficulty:** Easy
- **Latest accepted:** 2026-10-24 17:24 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-10-24 17:24 UTC | Python3 | 5 ms (40.6%) | 19.2 MB (51.2%) | [Code](solution-v1.py) |

---

### Description
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.


	For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


&nbsp;
Example 1:


Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.


Example 2:


Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.


&nbsp;
Constraints:


	0 &lt;= x &lt;= 231 - 1
