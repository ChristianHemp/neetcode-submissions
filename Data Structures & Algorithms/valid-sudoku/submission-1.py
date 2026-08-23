from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)   # maps row num to set of values
        cols = defaultdict(set)    # maps col num to set of values
        sub_boxes = defaultdict(set)   # maps subbox num to set of values

        for i in range(9):
            for j in range(9):
                if (board[i][j] in rows[i] or 
                    board[i][j] in cols[j] or
                    board[i][j] in sub_boxes[self.getSubbox(i, j)]):
                    return False
                elif board[i][j] != ".":
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    sub_boxes[self.getSubbox(i, j)].add(board[i][j])
        
        return True
    
    def getSubbox(self, i, j):
        if i <= 2 and j <= 2:
            return 0
        elif i <= 2 and j <= 5:
            return 1
        elif i <= 2 and j <= 8:
            return 2
        elif i <= 5 and j <= 2:
            return 3
        elif i <= 5 and j <= 5:
            return 4
        elif i <= 5 and j <= 8:
            return 5
        elif i <= 8 and j <= 2:
            return 6
        elif i <= 8 and j <= 5:
            return 7
        elif i <= 8 and j <= 8:
            return 8