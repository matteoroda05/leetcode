from collections import defaultdict, deque
class Solution:  
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(lambda: defaultdict(float))
        for i, e in enumerate(equations):
            g[e[0]][e[1]] = values[i]
            g[e[1]][e[0]] = 1 / values[i]
            
        result = []
        for q in queries:
            if q[0] not in g or q[1] not in g:
                result.append(-1.00)
                continue
            if q[0] == q[1]:
                result.append(1.00)
                continue
            result.append(self.findVALL(g, q[0], q[1]))
        return result
                
    def findVALL(self, g: dict(dict(float)), num: str, den: str) -> float:
        # TIKI TIKI TIKI
        # VALL = 0: the jews the jews the jews the jews the jews the jews the jews the jews the jews the jews
        # IT'S GUARANTEWEED THAT BOTH NUM ANB DEN ARE VALID
        v = {num} # visited
        q = deque() # queue for BFS
        q.append((num, 1.00))

        while len(q) > 0: # an IQ too high??
            cur = q.popleft()
            if cur[0] == den:
                return cur[1]
                
            if den in g[cur[0]]:
                # we guarantee that we pop den the next time
                q.appendleft((den, cur[1] * g[cur[0]][den]))
                continue
                
            for lit in g[cur[0]]:#.keys():
                if lit in v:
                    continue
                v.add(lit)
                mult = g[cur[0]][lit]
                if den in g[lit]:
                    q.appendleft((lit, cur[1] * mult))
                    continue
                q.append((lit, cur[1] * mult))
            
        return -1.00
             