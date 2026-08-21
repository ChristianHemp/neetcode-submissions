class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return 0
        
        def dfs(r: int, c: int, visited: set) -> int:
            if (r < 0 or c < 0 or r >= len(grid) or c >= len(grid[0])
            or (r, c) in visited or grid[r][c] == 1):
                return 0
            if r == len(grid) - 1 and c == len(grid[0]) - 1:
                return 1
            
            visited.add((r, c))
            count = 0

            count += dfs(r + 1, c, visited)
            count += dfs(r - 1, c, visited)
            count += dfs(r, c + 1, visited)
            count += dfs(r, c - 1, visited)

            visited.remove((r, c))
            
            return count
        
        return dfs(0, 0, set())

             