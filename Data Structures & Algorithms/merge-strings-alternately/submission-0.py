class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) == 0:
            return word2
        elif len(word2) == 0:
            return word1

        chars = []
        c1 = 0
        c2 = 0

        while c1 < len(word1) and c2 < len(word2):
            chars.append(word1[c1])
            chars.append(word2[c2])

            c1 += 1
            c2 += 1
        
        while c1 < len(word1):
            chars.append(word1[c1])
            c1 += 1
        
        while c2 < len(word2):
            chars.append(word2[c2])
            c2 += 1
        
        return ''.join(chars)