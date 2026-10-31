# [0230] Kth Smallest Element in a BST

- **Difficulty:** Medium
- **Latest accepted:** 2026-10-26 09:58 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-10-26 09:58 UTC | Python3 | 0 ms (100.0%) | 22.3 MB (25.3%) | [Code](solution-v1.py) |

---

### Description
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

&nbsp;
Example 1:


Input: root = [3,1,4,null,2], k = 1
Output: 1


Example 2:


Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3


&nbsp;
Constraints:


	The number of nodes in the tree is n.
	1 &lt;= k &lt;= n &lt;= 104
	0 &lt;= Node.val &lt;= 104


&nbsp;
Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?
