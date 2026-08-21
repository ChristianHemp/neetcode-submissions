class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        visited = set()
        length = 1

        q.append((0, 0))
        visited.add((0, 0))

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                if r == rows - 1 and c == cols - 1:
                    return length
                
                neighbor_directions = ((1, 0), (-1, 0), (0, 1), (0, -1),
                                       (1, 1), (-1, 1), (1, -1), (-1, -1))
                
                for dr, dc in neighbor_directions:
                    nr = r + dr
                    nc = c + dc
                    
                    if (nr < 0 or nc < 0 or nr >= rows or nc >= cols or
                        (nr, nc) in visited or grid[nr][nc] == 1):
                        continue
                    
                    q.append((nr, nc))
                    visited.add((nr, nc))
            length += 1
        
        return -1