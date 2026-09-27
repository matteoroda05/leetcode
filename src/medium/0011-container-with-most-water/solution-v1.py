class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        lMax = height[left]
        right = len(height) - 1
        rMax = height[right]

        maxw = (right - left) * min(lMax, rMax)
        
        while left < right:
            if lMax <= rMax:
                water = (right - left) * min(height[right], height[left])
                left +=1
            elif lMax > rMax:
                water = (right - left) * min(height[right], height[left])
                right -=1

            if water > maxw:
                maxw = water
            
            if height[left] > lMax:
                lMax = height[left]
            if height[right] > rMax:
                rMax = height[right]

        return maxw