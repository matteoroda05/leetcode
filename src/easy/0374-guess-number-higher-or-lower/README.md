# [0374] Guess Number Higher or Lower

- **Difficulty:** Easy
- **Latest accepted:** 2026-10-24 17:40 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-10-24 17:40 UTC | C | 1 ms (54.5%) | 8.4 MB (81.2%) | [Code](solution-v1.c) |

---

### Description
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked (the number I picked stays the same throughout the game).

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:


	-1: Your guess is higher than the number I picked (i.e. num &gt; pick).
	1: Your guess is lower than the number I picked (i.e. num &lt; pick).
	0: your guess is equal to the number I picked (i.e. num == pick).


Return the number that I picked.

&nbsp;
Example 1:


Input: n = 10, pick = 6
Output: 6


Example 2:


Input: n = 1, pick = 1
Output: 1


Example 3:


Input: n = 2, pick = 1
Output: 1


&nbsp;
Constraints:


	1 &lt;= n &lt;= 231 - 1
	1 &lt;= pick &lt;= n
