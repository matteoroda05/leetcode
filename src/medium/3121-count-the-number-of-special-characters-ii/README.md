# [3121] Count the Number of Special Characters II

- **Difficulty:** Medium
- **Latest accepted:** 2026-05-27 17:31 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-05-27 17:31 UTC | Python3 | 492 ms (8.9%) | 21.7 MB (10.7%) | [Code](solution-v1.py) |

---

### Description
You are given a string word. A letter&nbsp;c is called special if it appears both in lowercase and uppercase in word, and every lowercase occurrence of c appears before the first uppercase occurrence of c.

Return the number of special letters in word.

&nbsp;
Example 1:


Input: word = &quot;aaAbcBC&quot;

Output: 3

Explanation:

The special characters are &#39;a&#39;, &#39;b&#39;, and &#39;c&#39;.


Example 2:


Input: word = &quot;abc&quot;

Output: 0

Explanation:

There are no special characters in word.


Example 3:


Input: word = &quot;AbBCab&quot;

Output: 0

Explanation:

There are no special characters in word.


&nbsp;
Constraints:


	1 &lt;= word.length &lt;= 2 * 105
	word consists of only lowercase and uppercase English letters.
