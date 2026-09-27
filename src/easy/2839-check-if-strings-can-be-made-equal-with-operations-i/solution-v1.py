class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        sS1 = set()
        for c in s1:
            if c not in sS1:
                sS1.add(c)
        sS2 = set()
        for c in s2:
            if c not in sS2:
                sS2.add(c)
        
        if sS1 != sS2:
            return False
        
        firstCouple1 = {s1[0], s1[2]}
        firstCouple2 = {s2[0], s2[2]}
        if firstCouple1 != firstCouple2:
            return False
        
        lastCouple1 = {s1[1], s1[3]}
        lastCouple2 = {s2[1], s2[3]}
        if lastCouple1 != lastCouple2:
            return False

        return True