class Solution:
    def search1(self, nums: list[int], target: int) -> int:
        # this works, which is crazy:
        # return nums.index(target) if target in nums else -1

        def findFirstIndex (nums: list[int]):
            left,right = 0,len(nums)-1
            if nums[left] < nums[right]:
                return 0

            while left<right:
                mid = ceil((right+left)/2)
                if nums[mid] < nums[left]:
                    right = mid -1
                else:
                    left = mid
            return left+1

        delta = findFirstIndex(nums)
        size = len(nums)
        left, right = 0, size-1
        if target < nums[(left+delta)%size] or target > nums[(right+delta)%size]:
            return -1
        
        while left <= right:
            mid = floor((left+right)/2)

            if nums[(mid+delta)%size] < target:
                left = mid + 1
            elif nums[(mid+delta)%size] > target:
                right = mid -1
            else:
                return (mid + delta)%size
        return -1


    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)-1
    
        while left <= right:
            mid = math.floor((left+right)/2)
            cmid = nums[mid]
            
            if cmid == target:
                return mid
            
            if  cmid >= nums[left]:
                if  nums[left] <= target < cmid:
                    right = mid -1
                else:
                    left = mid + 1
            else:
                if  nums[right] >= target > cmid:
                    left = mid +1 
                else:
                    right = mid -1  
        
        return -1