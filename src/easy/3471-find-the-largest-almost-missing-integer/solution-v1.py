class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == len(nums):
            return max(nums)

        if k == 1:
            s = set()
            d = set()
            for n in nums:
                if n in s:
                    d.add(n)
                else:
                    s.add(n)
            for n in d:
                s.remove(n)
            if s:
                return max(s)
            return -1
            
        def isUnique(i: int, nums: List[int]) -> bool:
            if i in nums:
                return False
            return True
        
        s = len(nums)
        last = nums[s-1]
        first = nums[0]
        lU = isUnique(last, nums[:s-1])
        fU = isUnique(first, nums[1:])

        if fU and lU:
            return max(last, first)
        if fU:
            return first
        if lU:
            return last

        return -1