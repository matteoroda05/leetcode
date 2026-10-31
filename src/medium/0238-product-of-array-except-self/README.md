# [0238] Product of Array Except Self

- **Difficulty:** Medium
- **Latest accepted:** 2026-10-29 11:13 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-10-29 11:13 UTC | Python3 | 29 ms (35.6%) | 25.2 MB (82.9%) | [Code](solution-v1.py) |

---

### Description
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in&nbsp;O(n)&nbsp;time and without using the division operation.

&nbsp;
Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

&nbsp;
Constraints:


	2 &lt;= nums.length &lt;= 105
	-30 &lt;= nums[i] &lt;= 30
	The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.


&nbsp;
Follow up:&nbsp;Can you solve the problem in O(1)&nbsp;extra&nbsp;space complexity? (The output array does not count as extra space for space complexity analysis.)
