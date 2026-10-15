# [0002] Add Two Numbers

- **Difficulty:** Medium
- **Latest accepted:** 2026-10-13 17:07 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-10-13 17:07 UTC | Python3 | 3 ms (65.6%) | 19.2 MB (96.1%) | [Code](solution-v1.py) |

---

### Description
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum&nbsp;as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

&nbsp;
Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.


Example 2:


Input: l1 = [0], l2 = [0]
Output: [0]


Example 3:


Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]


&nbsp;
Constraints:


	The number of nodes in each linked list is in the range [1, 100].
	0 &lt;= Node.val &lt;= 9
	It is guaranteed that the list represents a number that does not have leading zeros.
