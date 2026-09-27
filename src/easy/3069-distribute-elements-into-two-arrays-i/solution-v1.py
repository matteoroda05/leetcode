class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1 = [nums[0]]
        arr2 = [nums[1]]
        len1 = 1
        len2 = 1
        lenNums = len(nums)
        idx = 2

        while len1 + len2 < lenNums:
            if arr1[len1 - 1] > arr2[len2 - 1]:
                arr1.append(nums[idx])
                len1+=1
            else:
                arr2.append(nums[idx])
                len2+=1
            idx+=1
        
        return arr1 + arr2