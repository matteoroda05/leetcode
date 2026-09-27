class Solution:
    def sum_digits3(self, n):
        r = 0
        while n:
            r, n = r + n % 10, n // 10
        return r

    def minElement(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            nums[i]=self.sum_digits3(n)
        
        nums.sort()
        return nums[0]