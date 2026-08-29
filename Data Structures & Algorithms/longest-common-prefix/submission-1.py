class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''

        longest = max(strs)
        shortest = min(strs)
        chars = []

        for i in range(len(shortest)):
            if shortest[i] == longest[i]:
                chars.append(shortest[i])
            else:
                break
        
        return ''.join(chars)