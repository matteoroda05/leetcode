class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prefix = {}
        for i, num in enumerate(nums):
            if num in prefix.keys():
                return [i, prefix[num]]
            
            prefix[target - num] = i


    def twoSums(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target:
                    return[i,j]

