class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        found = False

        def dfs(row, col, index):
            nonlocal found  # flag word found

            if (row < 0 or col < 0 or
            row == rows or col == cols or 
            board[row][col] == '%' or found == True or 
            board[row][col] != word[index]):
                return
            
            # mark index as seen in place to avoid using a set
            board[row][col] = '%'

            if index == len(word) - 1:
                found = True
                return

            dfs(row + 1, col, index + 1)
            dfs(row - 1, col, index + 1)
            dfs(row, col + 1, index + 1)
            dfs(row, col - 1, index + 1)

            # unmark the board (backtracking)
            board[row][col] = word[index]
        
        # first check if word is even possible in the grid
        if rows * cols >= len(word):
            for r in range(rows):
                for c in range(cols):
                    # only call dfs if char matches starting char in target word
                    if board[r][c] == word[0]:
                        dfs(r, c, 0)

                    if found == True:
                        return True
        
            return False
        else:
            return False