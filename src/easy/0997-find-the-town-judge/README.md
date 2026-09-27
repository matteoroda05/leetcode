# [0997] Find the Town Judge

- **Difficulty:** Easy
- **Latest accepted:** 2025-06-13 19:14 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2025-06-13 19:14 UTC | C | 0 ms (100.0%) | 19.6 MB (100.0%) | [Code](solution-v1.c) |

---

### Description
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:


	The town judge trusts nobody.
	Everybody (except for the town judge) trusts the town judge.
	There is exactly one person that satisfies properties 1 and 2.


You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

&nbsp;
Example 1:


Input: n = 2, trust = [[1,2]]
Output: 2


Example 2:


Input: n = 3, trust = [[1,3],[2,3]]
Output: 3


Example 3:


Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1


&nbsp;
Constraints:


	1 &lt;= n &lt;= 1000
	0 &lt;= trust.length &lt;= 104
	trust[i].length == 2
	All the pairs of trust are unique.
	ai != bi
	1 &lt;= ai, bi &lt;= n
