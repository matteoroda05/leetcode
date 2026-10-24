# [0199] Binary Tree Right Side View

- **Difficulty:** Medium
- **Latest accepted:** 2026-10-20 08:36 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-10-20 08:36 UTC | Python3 | 0 ms (100.0%) | 19.2 MB (67.5%) | [Code](solution-v1.py) |

---

### Description
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

&nbsp;
Example 1:


Input: root = [1,2,3,null,5,null,4]

Output: [1,3,4]

Explanation:




Example 2:


Input: root = [1,2,3,4,null,null,null,5]

Output: [1,3,4,5]

Explanation:




Example 3:


Input: root = [1,null,3]

Output: [1,3]


Example 4:


Input: root = []

Output: []


&nbsp;
Constraints:


	The number of nodes in the tree is in the range [0, 100].
	-100 &lt;= Node.val &lt;= 100
