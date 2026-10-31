from collections import deque
class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        # bfs/dijkstra: heap with minimum current bitwise or
        # dijksra CANNOT BE: it is not non-derecressing
        # no heap: otherwise logn added
        q = deque()
        q.append((grid[0][0], 0, 0))
        m, n = len(grid), len(grid[0])

        directions = [(1,0), (0,1)]
        mi = float('+inf')
        visited = {(grid[0][0], 0, 0)}
        while len(q) > 0: 
            cval, i, j = q.popleft()
            if i == m -1 and j == n-1:
                mi = cval if cval < mi else mi
            for d in directions: 
                if i+d[0] < m and j+d[1] < n:
                    tupl = (cval ^ grid[i+d[0]][j+d[1]], i+d[0], j+d[1])
                    if tupl not in visited:
                        q.append(tupl)
                        visited.add(tupl)

        return mi