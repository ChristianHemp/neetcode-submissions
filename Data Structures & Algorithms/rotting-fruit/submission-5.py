class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        minutes = 0
        fresh_count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh_count += 1
        
        # no fresh fruit in matrix
        if fresh_count == 0:
            return 0
        
        # no rotten fruit in matrix
        if not q:
            return -1

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                neighbor_directions = ((1, 0), (-1, 0), (0, 1), (0, -1))

                for dr, dc in neighbor_directions:
                    nr = r + dr
                    nc = c + dc

                    if (nr < 0 or nc < 0 or
                        nr >= rows or nc >= cols or
                        grid[nr][nc] == 0 or grid[nr][nc] == 2):
                        continue

                    grid[nr][nc] = 2
                    fresh_count -= 1
                    q.append((nr, nc))
            # prevents minutes from incrementing when bfs complete
            if q:
                minutes += 1
        
        # not all fresh fruit turned rotten
        if fresh_count != 0:
            return -1

        return minutes

