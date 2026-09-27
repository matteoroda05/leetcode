# [3612] Process String with Special Operations I

- **Difficulty:** Medium
- **Latest accepted:** 2026-06-16 16:38 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-06-16 16:38 UTC | Python3 | 0 ms (100.0%) | 23.3 MB (85.1%) | [Code](solution-v1.py) |

---

### Description
You are given a string s consisting of lowercase English letters and the special characters: *, #, and %.

Build a new string result by processing s according to the following rules from left to right:


	If the letter is a lowercase English letter append it to result.
	A &#39;*&#39; removes the last character from result, if it exists.
	A &#39;#&#39; duplicates the current result and appends it to itself.
	A &#39;%&#39; reverses the current result.


Return the final string result after processing all characters in s.

&nbsp;
Example 1:


Input: s = &quot;a#b%*&quot;

Output: &quot;ba&quot;

Explanation:


	
		
			i
			s[i]
			Operation
			Current result
		
	
	
		
			0
			&#39;a&#39;
			Append &#39;a&#39;
			&quot;a&quot;
		
		
			1
			&#39;#&#39;
			Duplicate result
			&quot;aa&quot;
		
		
			2
			&#39;b&#39;
			Append &#39;b&#39;
			&quot;aab&quot;
		
		
			3
			&#39;%&#39;
			Reverse result
			&quot;baa&quot;
		
		
			4
			&#39;*&#39;
			Remove the last character
			&quot;ba&quot;
		
	


Thus, the final result is &quot;ba&quot;.


Example 2:


Input: s = &quot;z*#&quot;

Output: &quot;&quot;

Explanation:


	
		
			i
			s[i]
			Operation
			Current result
		
	
	
		
			0
			&#39;z&#39;
			Append &#39;z&#39;
			&quot;z&quot;
		
		
			1
			&#39;*&#39;
			Remove the last character
			&quot;&quot;
		
		
			2
			&#39;#&#39;
			Duplicate the string
			&quot;&quot;
		
	


Thus, the final result is &quot;&quot;.


&nbsp;
Constraints:


	1 &lt;= s.length &lt;= 20
	s consists of only lowercase English letters and special characters *, #, and %.
