class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if i == sum([int(d) for d in str(n)]):
                return i
        return -1