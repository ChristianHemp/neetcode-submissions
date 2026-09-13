class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.word = True

    def search(self, word: str) -> bool:
        
        def dfs(root, i):
            curr = root

            for j in range(i, len(word)):
                c = word[j]

                # normal trie search
                if c != '.':
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
                # recursively search all children of curr for match
                else:
                    for val in curr.children.values():
                        if dfs(val, j + 1):
                            return True
                    return False
            return curr.word
        
        return dfs(self.root, 0)
