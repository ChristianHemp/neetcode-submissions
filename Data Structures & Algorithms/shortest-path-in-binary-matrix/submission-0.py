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
                
                neighbor_directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                                       (1, 1), (-1, 1), (1, -1), (-1, -1)]
                
                for dr, dc in neighbor_directions:
                    if (r + dr < 0 or c + dc < 0 or
                        r + dr >= rows or c + dc >= cols or
                        (r + dr, c + dc) in visited or 
                        grid[r + dr][c + dc] == 1):
                        continue
                    
                    q.append((r + dr, c + dc))
                    visited.add((r + dr, c + dc))
            length += 1
        
        return -1
