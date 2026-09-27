class Solution:
    def processStr(self, s: str) -> str:
        out = ""
        for i, c in enumerate(s):
            if c == '*':
                # FIX: Check if 'out' is not empty before removing the last character
                if out:
                    out = out[:len(out)-1]
            elif c == '%':
                out = out[::-1]
            elif c == '#':
                # FIX: Check if 'out' is not empty before duplicating the last character
                if out:
                    out += out
            else: 
                out += c
            
        return out