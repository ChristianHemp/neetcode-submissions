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
        for R in range(len(s2)):
            window[s2[R]] += 1

            if window == target:
                return True

            if R - L + 1 >= len(s1):
                window[s2[L]] -= 1

                # remove unused values from window for dict comparison
                if window[s2[L]] == 0:
                    del window[s2[L]]

                L += 1

        return False