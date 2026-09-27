class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        longest = 0

        # # brute force: for each element we check the longest substring
        # for i, c in enumerate(s):
        #     present = set()
        #     present.add(c)
        #     if i < len(s)-1:
        #         for c1 in s[i+1:]:
        #             if c1 in present:
        #                 break
        #             else:
        #                 present.add(c1)

        #     if len(present) > longest:
        #         longest = len (present)

        # ------
        # non brute force: sliding window 
        
        chars = {}
        current =0
        start = 0

        for i, c in enumerate(s):
            if c in chars and start <= chars [c]:
                current = i - chars[c]
                start = chars[c] + 1
                chars[c] = i
            else:
                chars[c]=i
                current +=1

            if current > longest:
                longest = current
        
        return longest