class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k, d = 0, 0
        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                d+=1
            else:
                k+=1
            
            nums[i-d]= n
        return k