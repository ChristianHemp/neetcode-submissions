class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == 0:
                return 0
            
            grid[row][col] = 0

            return (
                1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)
                )

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                result = max(result, dfs(r, c))
        
        return result

