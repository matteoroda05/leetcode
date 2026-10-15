class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        diz = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        res = diz[s[len(s)-1]]

        for i in range(0, len(s)-1):
            if diz[s[i]] < diz[s[i+1]]:
                res -= diz[s[i]]
            else: 
                res += diz[s[i]]

        return res