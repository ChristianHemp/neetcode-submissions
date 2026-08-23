from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)   # maps row num to set of values
        cols = defaultdict(set)    # maps col num to set of values
        sub_boxes = defaultdict(set)   # maps subbox tuple to set of values

        for i in range(9):
            for j in range(9):
                box = (i // 3, j // 3)

                if (board[i][j] in rows[i] or 
                    board[i][j] in cols[j] or
                    board[i][j] in sub_boxes[box]):
                    return False
                elif board[i][j] != ".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    sub_boxes[box].add(board[i][j])
        
        return True
