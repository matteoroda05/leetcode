class Solution:
    def checkValidString(self, s: str) -> bool:
        st = []
        op = []
        for i, c in enumerate(s):
            if c == '*':
                st.append(i)
            elif c == '(':
                op.append(i)
            else: # c == ')'
                if len(op) > 0:
                    op.pop()
                elif len(st) > 0:
                    st.pop()
                else: return False

        if len(op) == 0: return True

        while op and st:
            if op.pop() > st.pop():
                return False
        
        return len(op) == 0