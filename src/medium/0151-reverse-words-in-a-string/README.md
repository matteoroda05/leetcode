# [0151] Reverse Words in a String

- **Difficulty:** Medium
- **Latest accepted:** 2026-10-27 11:39 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-10-27 11:39 UTC | Python3 | 90 ms (6.4%) | 19.5 MB (10.3%) | [Code](solution-v1.py) |

---

### Description
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

&nbsp;
Example 1:


Input: s = &quot;the sky is blue&quot;
Output: &quot;blue is sky the&quot;


Example 2:


Input: s = &quot;  hello world  &quot;
Output: &quot;world hello&quot;
Explanation: Your reversed string should not contain leading or trailing spaces.


Example 3:


Input: s = &quot;a good   example&quot;
Output: &quot;example good a&quot;
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


&nbsp;
Constraints:


	1 &lt;= s.length &lt;= 104
	s contains English letters (upper-case and lower-case), digits, and spaces &#39; &#39;.
	There is at least one word in s.


&nbsp;
Follow-up:&nbsp;If the string data type is mutable in your language, can&nbsp;you solve it&nbsp;in-place&nbsp;with&nbsp;O(1)&nbsp;extra space?
