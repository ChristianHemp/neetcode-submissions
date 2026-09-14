class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root

        # Traverse trie for matching characters then create new children
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]

        curr.word = True

    def search(self, word: str) -> bool:
        curr = self.root

        # Traverse trie looking for char c
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        # True only if end of a word
        return curr.word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        # Traverse trie looking for char c
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return True
        