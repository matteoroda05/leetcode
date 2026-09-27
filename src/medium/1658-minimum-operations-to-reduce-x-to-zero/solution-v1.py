class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        if nums[0] > x and nums[-1] > x:
            return -1

        tot = sum(nums)
        size = len(nums)
        if tot < x:
            return -1
        elif tot == x:
            return size

        largest = 0
        prefix = tot-x
        cursum = 0
        i,j = 0,0

        while i <= j and j < size:
            cursum += nums[j]
            if cursum == prefix:
                largest = max(largest, j-i+1)
            else:
                while cursum > prefix and i < j:
                    cursum -= nums[i]
                    i +=1
                    if cursum == prefix:
                        largest = max(largest, j-i+1)
            j+=1

        if largest == 0:
            return -1
        return size - largest

        