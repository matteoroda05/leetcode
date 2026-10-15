class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        out = ""
        for chars in zip(*strs):
            c0=chars[0]
            for c in chars:
                if c != c0:
                    return out
            out+=c0
        return out