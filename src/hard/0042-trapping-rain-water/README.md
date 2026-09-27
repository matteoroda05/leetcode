# [0042] Trapping Rain Water

- **Difficulty:** Hard
- **Latest accepted:** 2026-08-16 11:01 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-08-16 11:01 UTC | Python3 | 7 ms (72.4%) | 21.2 MB (12.0%) | [Code](solution-v1.py) |

---

### Description
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

&nbsp;
Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.


Example 2:


Input: height = [4,2,0,3,2,5]
Output: 9


&nbsp;
Constraints:


	n == height.length
	1 &lt;= n &lt;= 2 * 104
	0 &lt;= height[i] &lt;= 105
