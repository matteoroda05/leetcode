# [0015] 3Sum

- **Difficulty:** Medium
- **Latest accepted:** 2026-08-16 17:14 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-08-16 17:14 UTC | Python3 | 1026 ms (15.7%) | 24.4 MB (5.3%) | [Code](solution-v1.py) |

---

### Description
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

&nbsp;
Example 1:


Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.


Example 2:


Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.


Example 3:


Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


&nbsp;
Constraints:


	3 &lt;= nums.length &lt;= 3000
	-105 &lt;= nums[i] &lt;= 105
