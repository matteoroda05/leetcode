# [3882] Minimum XOR Path in a Grid

- **Difficulty:** Medium
- **Latest accepted:** 2026-10-28 15:53 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-10-28 15:53 UTC | Python3 | 9225 ms (5.0%) | 165.3 MB (5.0%) | [Code](solution-v1.py) |

---

### Description
You are given a 2D integer array grid of size m * n.

You start at the top-left cell (0, 0) and want to reach the bottom-right cell (m - 1, n - 1).

At each step, you may move either right or down.

The cost of a path is defined as the bitwise XOR of all the values in the cells along that path, including the start and end cells.

Return the minimum possible XOR value among all valid paths from (0, 0) to (m - 1, n - 1).

&nbsp;
Example 1:


Input: grid = [[1,2],[3,4]]

Output: 6

Explanation:

There are two valid paths:


	(0, 0) &rarr; (0, 1) &rarr; (1, 1) with XOR: 1 XOR 2 XOR 4 = 7
	(0, 0) &rarr; (1, 0) &rarr; (1, 1) with XOR: 1 XOR 3 XOR 4 = 6


The minimum XOR value among all valid paths is 6.


Example 2:


Input: grid = [[6,7],[5,8]]

Output: 9

Explanation:

There are two valid paths:


	(0, 0) &rarr; (0, 1) &rarr; (1, 1) with XOR: 6 XOR 7 XOR 8 = 9
	(0, 0) &rarr; (1, 0) &rarr; (1, 1) with XOR: 6 XOR 5 XOR 8 = 11


The minimum XOR value among all valid paths is 9.


Example 3:


Input: grid = [[2,7,5]]

Output: 0

Explanation:

There is only one valid path:


	(0, 0) &rarr; (0, 1) &rarr; (0, 2) with XOR: 2 XOR 7 XOR 5 = 0


The XOR value of this path is 0, which is the minimum possible.


&nbsp;
Constraints:


	1 &lt;= m == grid.length &lt;= 1000
	1 &lt;= n == grid[i].length &lt;= 1000
	m * n &lt;= 1000
	0 &lt;= grid[i][j] &lt;= 1023​
