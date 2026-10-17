class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        oranges, rotten = 0, 0
        sizeI, sizeJ = len(grid), len(grid[0])

        fresh = set()
        for i, l in enumerate(grid):
            for j, c in enumerate(l):
                oranges += 1 if c > 0 else 0
                rotten += 1 if c == 2 else 0
                if c == 1:
                    fresh.add((i,j))

        if oranges == rotten:
            return 0 
        if oranges == 1 or rotten == 0:
            return -1

        prev_rotten = 0
        minutes= 0
        #  O((n*n)**2)
        vectors = [[0, -1], [0, 1], [-1, 0], [1, 0]]

        # loop until no more oranges rot 
        while rotten > prev_rotten:
            prev_rotten = rotten
            minutes += 1
            visited = set()

            # loop over the elements in 'fresh' and checkif they become rotten 
            for (fi, fj) in fresh:
                # if any([(fi, fj+1), (fi, fj-1), (fi+1, fj), (fi-1, fj)]) not in visited  and 
                for v in vectors:
                    if ( (fi+v[0], fj+v[1]) not in visited ) and (0 <= fi+v[0] < sizeI and 0 <= fj+v[1] < sizeJ) and grid[fi+v[0]][fj+v[1]] == 2:
                        grid[fi][fj] = 2        # make the orange rotten
                        visited.add((fi, fj))   # add the orange to visitedc
                        rotten +=1              # increment rotten
                        break

            fresh-=visited  # remove from fresh the visited and rotten oranges

        if oranges == rotten:
            return minutes -1
        return -1