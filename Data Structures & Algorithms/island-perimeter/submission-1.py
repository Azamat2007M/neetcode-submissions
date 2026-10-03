class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        #Itertive method Time: O(n*m) Space: O(1)
        rows = len(grid)
        cols = len(grid[0])
        perimetr = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimetr += 4

                    if r > 0 and grid[r - 1][c]:
                        perimetr -= 2

                    if c > 0 and grid[r][c - 1]:
                        perimetr -= 2
            
        return perimetr