class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #DFS method Time: O(n * m) Space: O(n * m)
        rows, cols = len(grid), len(grid[0])
        max_content = 0

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return False
            
            grid[r][c] = 0

            return (
                1 +
                dfs(r + 1, c) +
                dfs(r - 1, c) +
                dfs(r, c + 1) +
                dfs(r, c - 1)
            )

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_content = max(max_content, dfs(r, c))

        return max_content