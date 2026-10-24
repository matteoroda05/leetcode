# [0704] Binary Search

- **Difficulty:** Easy
- **Latest accepted:** 2026-10-24 10:52 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-10-24 10:52 UTC | Python3 | 0 ms (100.0%) | 20.4 MB (93.4%) | [Code](solution-v1.py) |

---

### Description
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

&nbsp;
Example 1:


Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4


Example 2:


Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1


&nbsp;
Constraints:


	1 &lt;= nums.length &lt;= 104
	-104 &lt; nums[i], target &lt; 104
	All the integers in nums are unique.
	nums is sorted in ascending order.
