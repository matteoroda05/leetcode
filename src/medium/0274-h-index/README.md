# [0274] H-Index

- **Difficulty:** Medium
- **Latest accepted:** 2026-10-09 14:37 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-10-09 14:37 UTC | Python3 | 0 ms (100.0%) | 19.7 MB (6.5%) | [Code](solution-v1.py) |

---

### Description
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher&#39;s h-index.

According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

&nbsp;
Example 1:


Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.


Example 2:


Input: citations = [1,3,1]
Output: 1


&nbsp;
Constraints:


	n == citations.length
	1 &lt;= n &lt;= 5000
	0 &lt;= citations[i] &lt;= 1000
