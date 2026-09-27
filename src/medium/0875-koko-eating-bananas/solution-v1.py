class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        high = max(piles)
        low = math.ceil(sum(piles)/h)
        size = len(piles)

        if h == size:
            return high

        while high > low:
            center = math.floor((high + low)/2)

            pileIndex = 0
            hourIndex = 0
            while hourIndex < h:
                if pileIndex == size:
                    break
                hourIndex += math.ceil(piles[pileIndex]/center)
                pileIndex += 1
                # we have finished eating all piles if on a given cycle we increment
                # pileIndex to size -> we check that now
            

            if pileIndex == size and hourIndex <= h:
                high = center
            
            else:
                low = center+1
        
        return low