# [0875] Koko Eating Bananas

- **Difficulty:** Medium
- **Latest accepted:** 2026-08-15 11:30 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-08-15 11:30 UTC | Python3 | 255 ms (5.1%) | 20.8 MB (13.7%) | [Code](solution-v1.py) |

---

### Description
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

&nbsp;
Example 1:


Input: piles = [3,6,7,11], h = 8
Output: 4


Example 2:


Input: piles = [30,11,23,4,20], h = 5
Output: 30


Example 3:


Input: piles = [30,11,23,4,20], h = 6
Output: 23


&nbsp;
Constraints:


	1 &lt;= piles.length &lt;= 104
	piles.length &lt;= h &lt;= 109
	1 &lt;= piles[i] &lt;= 109
