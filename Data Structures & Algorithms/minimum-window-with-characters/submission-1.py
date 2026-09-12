from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        counts = defaultdict(int)
        window = defaultdict(int)

        for c in t:
            counts[c] += 1

        matching_chars = 0
        sol_left, sol_right = None, None
        L = 0

        for R in range(len(s)):
            c = s[R]
            window[c] += 1

            if c in counts and window[c] == counts[c]:
                matching_chars += 1
            
            while matching_chars == len(counts):
                if sol_left is None and sol_right is None:
                    sol_left, sol_right = L, R
                elif (R - L) < (sol_right - sol_left):
                    sol_left, sol_right = L, R
                
                window[s[L]] -= 1
                if s[L] in counts and window[s[L]] < counts[s[L]]:
                    matching_chars -= 1
                L += 1
        
        if sol_left is None:
            return ""
        else:
            return s[sol_left:sol_right+1]