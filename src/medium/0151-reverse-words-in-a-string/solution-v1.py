class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        i = 0 
        
        while i < len(s):
            if s[i] == ' ':
                i+=1
                continue
            word = []
            while i < len(s) and s[i] != ' ':
                word.append(s[i])
                i+=1
            stack.append("".join(word))
            print(stack)
        
        return " ".join(stack[::-1])