# [0011] Container With Most Water

- **Difficulty:** Medium
- **Latest accepted:** 2026-09-25 21:27 UTC
- **Resubmissions (>48 hours):** 1

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-08-16 14:27 UTC | Python3 | 53 ms (77.1%) | 29.3 MB (97.9%) | [Code](solution-v1.py) |
| v2 | 2026-09-25 21:27 UTC | Python3 | 44 ms (94.1%) | 29.7 MB (15.3%) | [Code](solution-v2.py) |

---

### Description
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

&nbsp;
Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.


Example 2:


Input: height = [1,1]
Output: 1


&nbsp;
Constraints:


	n == height.length
	2 &lt;= n &lt;= 105
	0 &lt;= height[i] &lt;= 104
