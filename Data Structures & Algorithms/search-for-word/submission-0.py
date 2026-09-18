class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()
        found = False

        def dfs(row, col, index):
            nonlocal found

            if (row < 0 or col < 0 or
            row == rows or col == cols or 
            (row, col) in visited or found == True or 
            board[row][col] != word[index]):
                return
            
            visited.add((row, col))

            if index == len(word) - 1:
                found = True
                return

            dfs(row + 1, col, index + 1)
            dfs(row - 1, col, index + 1)
            dfs(row, col + 1, index + 1)
            dfs(row, col - 1, index + 1)

            visited.remove((row, col))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, 0)
                if found == True:
                    return True
        
        return False