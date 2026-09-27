# [0033] Search in Rotated Sorted Array

- **Difficulty:** Medium
- **Latest accepted:** 2026-09-25 16:20 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-09-25 16:20 UTC | Python3 | 0 ms (100.0%) | 19.8 MB (11.1%) | [Code](solution-v1.py) |

---

### Description
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 &lt;= k &lt; nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by&nbsp;3&nbsp;indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

&nbsp;
Example 1:
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:
Input: nums = [1], target = 0
Output: -1

&nbsp;
Constraints:


	1 &lt;= nums.length &lt;= 5000
	-104 &lt;= nums[i] &lt;= 104
	All values of nums are unique.
	nums is an ascending array that is possibly rotated.
	-104 &lt;= target &lt;= 104
