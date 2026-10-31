class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        size = len(nums)
        out = [1]*size
        leftmul = 1
        rightmul = 1
        for i in range(size):
            out[i]*=leftmul
            out[size-1 -i]*=rightmul
            leftmul*=nums[i]
            rightmul*=nums[size-1 -i]
        return out
    
    def productExceptSelfBruteforce(self, nums: list[int]) -> list[int]:
        out = []
        size = len(nums)
        for i in range(size):
            out.append(math.prod(nums[0:i]) * math.prod(nums[i+1:size]))
        return out