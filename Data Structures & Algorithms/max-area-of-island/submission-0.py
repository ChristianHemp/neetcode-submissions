class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        curr_size = 0
        res = 0

        def dfs(r, c):
            nonlocal curr_size

            if (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0]) or
            grid[r][c] == 0):
                return
            
            grid[r][c] = 0
            curr_size += 1

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    res = max(res, curr_size)
                    curr_size = 0
        
        return res
