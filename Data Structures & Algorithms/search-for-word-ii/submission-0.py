class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
    
    def addWord(self, word):
        curr = self

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()

        for word in words:
            root.addWord(word)

        rows, cols = len(board), len(board[0])
        res, visited = set(), set()

        def dfs(row, col, node, curr_word):
            if(row < 0 or col < 0 or
            row == rows or col == cols or
            (row, col) in visited or board[row][col] not in node.children):
                return
            
            visited.add((row, col))
            node = node.children[board[row][col]]
            # Update current word and check if word found
            curr_word += board[row][col]
            if node.end:
                res.add(curr_word)
            
            # Search all 4 directions
            dfs(row + 1, col, node, curr_word)
            dfs(row - 1, col, node, curr_word)
            dfs(row, col + 1, node, curr_word)
            dfs(row, col - 1, node, curr_word)

            visited.remove((row, col))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, '')
        
        return list(res)