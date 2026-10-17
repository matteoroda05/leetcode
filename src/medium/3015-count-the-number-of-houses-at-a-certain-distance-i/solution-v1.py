class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        out = [0] * (n)

        # def bfs(cur: int, curlen: int, n: int, x: int, y: int, visited, out: List[int], h[list]):
        #     if curlen > n or visited.get(cur, False) or cur > n or cur < 0:
        #         return

        #     if curlen > 0:
        #         out[curlen-1]+=1

        #     visited[cur] = True

        #     if cur == x and y not in range(x-1, x+2):
        #         bfs(y, curlen+1, n, x, y, visited, out)

        #     if cur == y and x not in range(y-1, y+2):
        #         bfs(y, curlen+1, n, x, y, visited, out)

        #     bfs(cur+1 , curlen+1, n, x, y, visited, out)
        #     bfs(cur-1 , curlen+1, n, x, y, visited, out)

        for i in range(1, n+1):
            visited = {}
            h = []
            heapq.heappush(h, (0, i))
            while h:
                c = heapq.heappop(h)
                if visited.get(c[1], False) or c[1] > n or c[1] < 1:
                    continue
                if c[0] > 0:
                    out[c[0]-1] += 1
                visited[c[1]] = True
                
                heapq.heappush(h, (c[0]+1, c[1]+1))
                heapq.heappush(h, (c[0]+1, c[1]-1))

                if c[1] == x:
                    heapq.heappush(h, (c[0]+1, y))
                if c[1] == y:
                    heapq.heappush(h, (c[0]+1, x))
        return out