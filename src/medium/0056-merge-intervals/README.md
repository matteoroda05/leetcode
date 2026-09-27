# [0056] Merge Intervals

- **Difficulty:** Medium
- **Latest accepted:** 2026-09-24 08:03 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-09-24 08:03 UTC | Python3 | 11 ms (26.0%) | 23.2 MB (30.2%) | [Code](solution-v1.py) |

---

### Description
Given an array&nbsp;of intervals&nbsp;where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

&nbsp;
Example 1:


Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].


Example 2:


Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.


Example 3:


Input: intervals = [[4,7],[1,4]]
Output: [[1,7]]
Explanation: Intervals [1,4] and [4,7] are considered overlapping.


&nbsp;
Constraints:


	1 &lt;= intervals.length &lt;= 104
	intervals[i].length == 2
	0 &lt;= starti &lt;= endi &lt;= 104
