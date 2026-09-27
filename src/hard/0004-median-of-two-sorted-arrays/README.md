# [0004] Median of Two Sorted Arrays

- **Difficulty:** Hard
- **Latest accepted:** 2025-11-03 11:42 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2025-11-03 11:42 UTC | C | 0 ms (100.0%) | 11.2 MB (100.0%) | [Code](solution-v1.c) |

---

### Description
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

&nbsp;
Example 1:


Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.


Example 2:


Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


&nbsp;
Constraints:


	nums1.length == m
	nums2.length == n
	0 &lt;= m &lt;= 1000
	0 &lt;= n &lt;= 1000
	1 &lt;= m + n &lt;= 2000
	-106 &lt;= nums1[i], nums2[i] &lt;= 106
