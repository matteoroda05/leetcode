# [3875] Construct Uniform Parity Array I

- **Difficulty:** Easy
- **Latest accepted:** 2026-09-02 14:28 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-09-02 14:28 UTC | Python3 | 0 ms (100.0%) | 19.2 MB (86.7%) | [Code](solution-v1.py) |

---

### Description
You are given an array nums1 of n distinct integers.

You want to construct another array nums2 of length n such that the elements in nums2 are either all odd or all even.

For each index i, you must choose exactly one of the following (in any order):


	nums2[i] = nums1[i]
	nums2[i] = nums1[i] - nums1[j], for an index j != i


Return true if it is possible to construct such an array, otherwise, return false.

&nbsp;
Example 1:


Input: nums1 = [2,3]

Output: true

Explanation:


	Choose nums2[0] = nums1[0] - nums1[1] = 2 - 3 = -1.
	Choose nums2[1] = nums1[1] = 3.
	nums2 = [-1, 3], and both elements are odd. Thus, the answer is true​​​​​​​.



Example 2:


Input: nums1 = [4,6]

Output: true

Explanation:​​​​​​​


	Choose nums2[0] = nums1[0] = 4.
	Choose nums2[1] = nums1[1] = 6.
	nums2 = [4, 6], and all elements are even. Thus, the answer is true.



&nbsp;
Constraints:


	1 &lt;= n == nums1.length &lt;= 100
	1 &lt;= nums1[i] &lt;= 100
	nums1 consists of distinct integers.
