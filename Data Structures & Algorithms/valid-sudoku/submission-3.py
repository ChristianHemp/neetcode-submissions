from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sections = defaultdict(set)
        rows = defaultdict(set)
        cols = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    continue
                
                val = board[i][j]
                section = (i // 3, j // 3)

                if val in rows[i] or val in cols[j] or val in sections[section]:
                    return False
                
                rows[i].add(val)
                cols[j].add(val)
                sections[section].add(val)
        
        return True