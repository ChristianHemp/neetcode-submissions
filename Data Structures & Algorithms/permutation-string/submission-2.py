from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = defaultdict(int)
        window = defaultdict(int)

        for c in s1:
            target[c] += 1
        
        L = 0
        matching_chars = 0

        for R in range(len(s2)):
            window[s2[R]] += 1

            if s2[R] in target and window[s2[R]] <= target[s2[R]]:
                matching_chars += 1

            if R - L + 1 > len(s1):
                if s2[L] in target and window[s2[L]] <= target[s2[L]]:
                    matching_chars -= 1
                
                window[s2[L]] -= 1
                L += 1
            
            if matching_chars == len(s1):
                return True

        return False