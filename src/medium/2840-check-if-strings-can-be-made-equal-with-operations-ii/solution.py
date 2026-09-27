class Solution:
    def checkStringsMine(self, s1: str, s2: str) -> bool:
        even = Counter()
        odd = Counter()
        for i, c in enumerate(s1):
            if i%2 == 0:
                even[c]+=1
            else:
                odd[c]+=1
        
        for i, c in enumerate(s2):
            if i%2 == 0:
                even[c]-=1
            else:
                odd[c]-=1

        for v in even.values():
            if v != 0:
                return False
        for v in odd.values():
            if v != 0:
                return False
        return True
        
    def checkStrings(self, s1: str, s2: str) -> bool:
        # Compare even indices
        if Counter(s1[::2]) != Counter(s2[::2]):
            return False
            
        # Compare odd indices
        if Counter(s1[1::2]) != Counter(s2[1::2]):
            return False
            
        return True