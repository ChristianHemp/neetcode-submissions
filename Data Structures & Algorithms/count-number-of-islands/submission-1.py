class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        def dfs(row, col):
            if col < 0 or row < 0 or row >= len(grid) or col >= len(grid[0]):
                return
            
            if grid[row][col] == '0':
                return
            
            if grid[row][col] == '1':
                grid[row][col] = 0

                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        
        return count
            

