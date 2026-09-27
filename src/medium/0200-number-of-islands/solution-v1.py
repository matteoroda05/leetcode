class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0

        m = len(grid)
        n = len(grid[0])

        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == "1":
                    islands +=1
                    self.coverIsland(grid, m, n, i, j)

        return islands
    
    def coverIsland (self, grid: List[List[str]], m: int, n: int, i: int, j: int) -> void:
        grid[i][j] = "0"

        if i < m-1:
            if grid[i+1][j] == "1":
                self.coverIsland(grid, m, n, i+1, j)
        if j < n-1: 
            if grid[i][j+1] == "1":
                self.coverIsland(grid, m, n, i, j+1)
        if j > 0:
            if grid[i][j-1] == "1":
                self.coverIsland(grid, m, n, i, j-1)
        if i > 0:
            if grid[i-1][j] == "1":
                self.coverIsland(grid, m, n, i-1, j)