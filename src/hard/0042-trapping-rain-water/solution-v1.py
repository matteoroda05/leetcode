class Solution:
    def trap1(self, height: List[int]) -> int:
        water = 0 

        hMap = {} # maps heights -> count heights
        maxH = 0

        for h in height:
            # if it's not the maximum add it to the map then execute the filling cycle
            if h < maxH:
                if h in hMap:
                    hMap[h] += 1
                else:
                    hMap[h] = 1
                # fill the gaps: 
                # - for each smaller key in the dictionary update the water by count * diff
                # - then update count for h and pop h
                for k in list(hMap.keys()):
                    if k < h:
                        water += (h - k) * hMap[k]
                        hMap[h] += hMap[k]
                        hMap.pop(k)
            
            if h >= maxH:
                for k in list(hMap.keys()):
                    water += (maxH - k) * hMap[k]
                    hMap.pop(k)

                # the map is now empty
                maxH = h

        return water

    def trap(self, height: List[int]) -> int:
        water = 0 
        left = 0
        lMax = height[left]
        right = len(height) - 1
        rMax = height[right]

        while left < right:
            if lMax <= rMax:
                water += lMax - height[left]
                left +=1
            elif lMax > rMax:
                water += rMax - height[right]
                right -=1

            
            if height[left] > lMax:
                lMax = height[left]
            if height[right] > rMax:
                rMax = height[right]

        return water
        