class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = []
        score = 0
        depth = 0
        i= 0
        while i < len(s):
            if s[i] == '(':
                st.append(depth)
                depth +=1
            else:
                curD = st.pop()
                depth -=1
                score += 2**curD
                while i < len(s) - 1 and s[i+1] == ')':
                    i+=1
                    st.pop()
                    depth -=1
            i+=1

        return score
