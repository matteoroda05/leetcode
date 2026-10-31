# [0769] Max Chunks To Make Sorted

- **Difficulty:** Medium
- **Latest accepted:** 2026-10-28 13:37 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-10-28 13:37 UTC | Python3 | 0 ms (100.0%) | 19.1 MB (92.8%) | [Code](solution-v1.py) |

---

### Description
You are given an integer array arr of length n that represents a permutation of the integers in the range [0, n - 1].

We split arr into some number of chunks (i.e., partitions), and individually sort each chunk. After concatenating them, the result should equal the sorted array.

Return the largest number of chunks we can make to sort the array.

&nbsp;
Example 1:


Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], which isn&#39;t sorted.


Example 2:


Input: arr = [1,0,2,3,4]
Output: 4
Explanation:
We can split into two chunks, such as [1, 0], [2, 3, 4].
However, splitting into [1, 0], [2], [3], [4] is the highest number of chunks possible.


&nbsp;
Constraints:


	n == arr.length
	1 &lt;= n &lt;= 10
	0 &lt;= arr[i] &lt; n
	All the elements of arr are unique.
