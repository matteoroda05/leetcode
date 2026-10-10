class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        o, count = 0, 0
        for c in s:
            if c =='(':
                o += 1
            elif o > 0: 
                o -=1
            else:
                count +=1
        return o + count