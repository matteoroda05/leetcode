# [0094] Binary Tree Inorder Traversal

- **Difficulty:** Easy
- **Latest accepted:** 2026-10-17 14:44 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-10-17 14:44 UTC | Python3 | 0 ms (100.0%) | 19.3 MB (26.3%) | [Code](solution-v1.py) |

---

### Description
Given the root of a binary tree, return the inorder traversal of its nodes&#39; values.

&nbsp;
Example 1:


Input: root = [1,null,2,3]

Output: [1,3,2]

Explanation:




Example 2:


Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]

Output: [4,2,6,5,7,1,3,9,8]

Explanation:




Example 3:


Input: root = []

Output: []


Example 4:


Input: root = [1]

Output: [1]


&nbsp;
Constraints:


	The number of nodes in the tree is in the range [0, 100].
	-100 &lt;= Node.val &lt;= 100


&nbsp;
Follow up: Recursive solution is trivial, could you do it iteratively?
