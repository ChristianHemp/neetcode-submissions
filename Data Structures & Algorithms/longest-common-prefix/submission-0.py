class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ''

        if len(strs) == 0:
            return lcp

        longest = max(strs)
        shortest = min(strs)

        for i in range(len(shortest)):
            if shortest[i] == longest[i]:
                lcp += shortest[i]
            else:
                break
        
        return lcp