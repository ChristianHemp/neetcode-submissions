from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts_s = defaultdict(int)
        counts_t = defaultdict(int)

        for i in range(len(s)):
            counts_s[s[i]] += 1
            counts_t[t[i]] += 1
        
        for key, value in counts_s.items():
            if value != counts_t[key]:
                return False
        
        return True