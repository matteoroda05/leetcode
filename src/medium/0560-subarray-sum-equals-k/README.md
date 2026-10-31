# [0560] Subarray Sum Equals K

- **Difficulty:** Medium
- **Latest accepted:** 2026-10-29 11:01 UTC
- **Resubmissions (>48 hours):** 1

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-10-14 15:39 UTC | Python3 | 35 ms (47.0%) | 21.9 MB (53.6%) | [Code](solution-v1.py) |
| v2 | 2026-10-29 11:01 UTC | Python3 | 36 ms (36.7%) | 21.5 MB (97.2%) | [Code](solution-v2.py) |

---

### Description
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.

&nbsp;
Example 1:
Input: nums = [1,1,1], k = 2
Output: 2
Example 2:
Input: nums = [1,2,3], k = 3
Output: 2

&nbsp;
Constraints:


	1 &lt;= nums.length &lt;= 2 * 104
	-1000 &lt;= nums[i] &lt;= 1000
	-107 &lt;= k &lt;= 107
