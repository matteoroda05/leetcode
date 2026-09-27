# [1200] Minimum Absolute Difference

- **Difficulty:** Easy
- **Latest accepted:** 2026-01-26 11:15 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-01-26 11:15 UTC | Python | 63 ms (91.7%) | 21.6 MB (44.9%) | [Code](solution-v1.py) |

---

### Description
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows


	a, b are from arr
	a &lt; b
	b - a equals to the minimum absolute difference of any two elements in arr


&nbsp;
Example 1:


Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

Example 2:


Input: arr = [1,3,6,10,15]
Output: [[1,3]]


Example 3:


Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]


&nbsp;
Constraints:


	2 &lt;= arr.length &lt;= 105
	-106 &lt;= arr[i] &lt;= 106
