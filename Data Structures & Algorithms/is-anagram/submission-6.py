from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        string_s_counts = defaultdict(int)
        string_t_counts = defaultdict(int)

        for index in range(len(s)):
            string_s_counts[s[index]] += 1
            string_t_counts[t[index]] += 1
        
        return string_s_counts == string_t_counts