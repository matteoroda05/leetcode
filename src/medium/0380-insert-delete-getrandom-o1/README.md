# [0380] Insert Delete GetRandom O(1)

- **Difficulty:** Medium
- **Latest accepted:** 2026-10-10 20:21 UTC
- **Resubmissions (>48 hours):** 0

### Submission history

Each version holds the latest accepted submission in its 48-hour window.
A submission more than 48 hours after that window began starts a new version.

| Version | Accepted (UTC) | Language | Runtime | Memory | Solution |
| :---: | :--- | :--- | :--- | :--- | :--- |
| v1 | 2026-10-10 20:21 UTC | Python3 | 84 ms (89.6%) | 57 MB (45.3%) | [Code](solution-v1.py) |

---

### Description
Implement the RandomizedSet class:


	RandomizedSet() Initializes the RandomizedSet object.
	bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
	bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
	int getRandom() Returns a random element from the current set of elements (it&#39;s guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.


You must implement the functions of the class such that each function works in&nbsp;average&nbsp;O(1)&nbsp;time complexity.

&nbsp;
Example 1:


Input
[&quot;RandomizedSet&quot;, &quot;insert&quot;, &quot;remove&quot;, &quot;insert&quot;, &quot;getRandom&quot;, &quot;remove&quot;, &quot;insert&quot;, &quot;getRandom&quot;]
[[], [1], [2], [2], [], [1], [2], []]
Output
[null, true, false, true, 2, true, false, 2]

Explanation
RandomizedSet randomizedSet = new RandomizedSet();
randomizedSet.insert(1); // Inserts 1 to the set. Returns true as 1 was inserted successfully.
randomizedSet.remove(2); // Returns false as 2 does not exist in the set.
randomizedSet.insert(2); // Inserts 2 to the set, returns true. Set now contains [1,2].
randomizedSet.getRandom(); // getRandom() should return either 1 or 2 randomly.
randomizedSet.remove(1); // Removes 1 from the set, returns true. Set now contains [2].
randomizedSet.insert(2); // 2 was already in the set, so return false.
randomizedSet.getRandom(); // Since 2 is the only number in the set, getRandom() will always return 2.


&nbsp;
Constraints:


	-231 &lt;= val &lt;= 231 - 1
	At most 2 *&nbsp;105 calls will be made to insert, remove, and getRandom.
	There will be at least one element in the data structure when getRandom is called.
