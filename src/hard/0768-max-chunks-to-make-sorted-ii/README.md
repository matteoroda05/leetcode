# [0768] Max Chunks To Make Sorted II

- **Difficulty:** Hard
- **Latest accepted:** 2026-10-28 14:29 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-10-28 14:29 UTC | Python3 | 4 ms (49.6%) | 19.3 MB (92.4%) | [Code](solution-v1.py) |

---

### Description
You are given an integer array arr.

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.

&nbsp;
Example 1:


Input: arr = [5,4,3,2,1]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in [4, 5, 1, 2, 3], which isn&#39;t sorted.


Example 2:


Input: arr = [2,1,3,4,4]
Output: 4
Explanation:
We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number of chunks possible.


&nbsp;
Constraints:


	1 &lt;= arr.length &lt;= 2000
	0 &lt;= arr[i] &lt;= 108
