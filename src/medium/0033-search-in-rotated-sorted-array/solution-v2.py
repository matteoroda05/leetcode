class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)-1
    
        while left <= right:
            mid = (left+right) >> 1
            if nums[mid] == target:
                return mid
            if nums[left]<=nums[mid]<=nums[right]:
                if nums[mid] < target:
                    left = mid + 1
                else: 
                    right = mid -1
            elif nums[mid] < nums[left]:
                # we're in the right-sorted part of the array
                if nums[mid] < target <= nums[right]:
                    left = mid +1
                else:
                    right = mid -1
            else: # nums[mid] > nums[right]:
                # left-sorted part of the array
                if nums[left] <= target < nums[mid]:
                    right = mid -1
                else:
                    left = mid +1
        
        return -1