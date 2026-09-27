# [0121] Best Time to Buy and Sell Stock

- **Difficulty:** Easy
- **Latest accepted:** 2026-09-24 10:11 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-09-24 10:11 UTC | Python3 | 29 ms (86.2%) | 28.7 MB (43.3%) | [Code](solution-v1.py) |

---

### Description
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

&nbsp;
Example 1:


Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


Example 2:


Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.


&nbsp;
Constraints:


	1 &lt;= prices.length &lt;= 105
	0 &lt;= prices[i] &lt;= 104
