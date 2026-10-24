class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r, mid = 0, len(nums)-1, floor(len(nums)/2)
        
        while l <= r:
            if nums[mid] == target: 
                return mid
            if nums[mid] > target:
                r = mid-1
            else:
                l = mid+1
            
            mid = floor((l+r)/2)
        return -1
