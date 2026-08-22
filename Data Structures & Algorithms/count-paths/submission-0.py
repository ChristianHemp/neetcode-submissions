class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev_row = [0] * n

        # start from bottom row and build "matrix" up (only keep prev_row)
        for row in range(m - 1, -1, -1):
            curr_row = [0] * n
            curr_row[n - 1] = 1

            # update curr_row based on values in down and right directions
            for col in range(n - 2, -1, -1):
                curr_row[col] = prev_row[col] + curr_row[col + 1]
            
            prev_row = curr_row
        
        return curr_row[0]