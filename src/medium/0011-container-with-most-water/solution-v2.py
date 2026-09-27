class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxw = (right - left) * min(height[right], height[left])
        
        while left < right:
            if height[left] <= height[right]:
                left +=1
            else:
                right -=1

            water = (right - left) * min(height[right], height[left])
            if water > maxw:
                maxw = water

        return maxw