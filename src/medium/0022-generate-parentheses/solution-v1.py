class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def generateNext(n: int, o: int, c: int) -> list[str]:
            out = []
            if o > 0 and c < o:
                nextlist = generateNext(n, o, c+1)
                for s in nextlist:
                    out.append(")" + s)
            if o < n:
                nextlist = generateNext(n, o+1, c)
                for s in nextlist:
                    out.append("(" + s)

            return [""] if len(out) == 0 else out
        
        return generateNext(n, 0, 0)