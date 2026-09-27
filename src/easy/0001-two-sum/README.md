# [0001] Two Sum

- **Difficulty:** Easy
- **Latest accepted:** 2026-08-16 14:39 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-08-16 14:39 UTC | Python3 | 0 ms (100.0%) | 20.9 MB (7.6%) | [Code](solution-v1.py) |

---

### Description
You are given an array of integers nums&nbsp;and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

&nbsp;
Example 1:


Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


Example 2:


Input: nums = [3,2,4], target = 6
Output: [1,2]


Example 3:


Input: nums = [3,3], target = 6
Output: [0,1]


&nbsp;
Constraints:


	2 &lt;= nums.length &lt;= 104
	-109 &lt;= nums[i] &lt;= 109
	-109 &lt;= target &lt;= 109
	Only one valid answer exists.


&nbsp;
Follow-up:&nbsp;Can you come up with an algorithm that is less than O(n2)&nbsp;time complexity?
