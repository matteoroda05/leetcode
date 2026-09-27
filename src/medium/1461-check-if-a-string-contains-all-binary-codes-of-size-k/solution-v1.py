class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """

        all_codes = 1 << k

        if len(s) < k + all_codes - 1:
            return False

        all = set()

        for i in range(len(s)-k+1):
            all.add(s[i:i+k])
            if len(all) == all_codes:
                return True

        if len(all) == all_codes:
            return True

        return False
        