class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        lowest_odd = inf
        lowest_even = inf
        for n in nums1:
            if n%2 == 0 and n < lowest_even:
                lowest_even = n 
            elif n%2 != 0 and n < lowest_odd:
                lowest_odd = n
        
        if lowest_odd == inf or lowest_odd < lowest_even:
            return True
        return False
                