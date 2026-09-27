class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k, d = 0, 0
        current = (0,0)
        for i, n in enumerate(nums):
            if current[0] == n and current[1] >= 2:
                d+=1
            else:
                k+=1

            if n != current[0]:
                current = (n, 1)
            else:
                current = (n, current[1] + 1)
            nums[i-d] = n
        return k