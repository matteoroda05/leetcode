# [3300] Minimum Element After Replacement With Digit Sum

- **Difficulty:** Easy
- **Latest accepted:** 2026-05-29 15:01 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-05-29 15:01 UTC | Python3 | 6 ms (32.9%) | 19.1 MB (91.5%) | [Code](solution-v1.py) |

---

### Description
You are given an integer array nums.

You replace each element in nums with the sum of its digits.

Return the minimum element in nums after all replacements.

&nbsp;
Example 1:


Input: nums = [10,12,13,14]

Output: 1

Explanation:

nums becomes [1, 3, 4, 5] after all replacements, with minimum element 1.


Example 2:


Input: nums = [1,2,3,4]

Output: 1

Explanation:

nums becomes [1, 2, 3, 4] after all replacements, with minimum element 1.


Example 3:


Input: nums = [999,19,199]

Output: 10

Explanation:

nums becomes [27, 10, 19] after all replacements, with minimum element 10.


&nbsp;
Constraints:


	1 &lt;= nums.length &lt;= 100
	1 &lt;= nums[i] &lt;= 104
