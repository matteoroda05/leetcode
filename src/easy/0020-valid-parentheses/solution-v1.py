class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for c in s:
            if c == '(' or c =='[' or c == '{':
                st.append(c)
            elif not st:
                return False
            else:
                p = st.pop()
                if (p == '(' and c != ')') or (p == '[' and c != ']') or (p == '{' and c != '}'):
                    return False

        return len(st) == 0