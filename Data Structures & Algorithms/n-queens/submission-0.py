class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        res = []

        used_cols = set()
        used_pos_diags = set()
        used_neg_diags = set()

        board = [['.'] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                copy = [''.join(row) for row in board]
                res.append(copy)
                return
            

            for c in range(n):
                if c in used_cols or r + c in used_pos_diags or r - c in used_neg_diags:
                    continue
                
                board[r][c] = 'Q'
                used_cols.add(c)
                used_pos_diags.add(r + c)
                used_neg_diags.add(r - c)

                backtrack(r + 1)

                board[r][c] = '.'
                used_cols.remove(c)
                used_pos_diags.remove(r + c)
                used_neg_diags.remove(r - c)

        backtrack(0)
        return res