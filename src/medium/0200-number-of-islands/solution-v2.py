class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count +=1
                    def dosomething(grid, i, j):
                        grid[i][j] = '2'
                        if i < len(grid) -1 and grid[i+1][j] == '1':
                            print ("0 did")
                            dosomething(grid, i+1, j)
                        if i > 0 and grid[i-1][j] == '1':
                            print ("1 did")
                            dosomething(grid, i-1, j)
                        if j < len(grid[0]) -1 and grid[i][j+1] == '1':
                            print ("2 did")
                            dosomething(grid, i, j+1)
                        if j > 0 and grid[i][j-1] == '1':
                            print ("3 did")
                            dosomething(grid, i, j-1)
                    dosomething(grid, i, j)

        return count