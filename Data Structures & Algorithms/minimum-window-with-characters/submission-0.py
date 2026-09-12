from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        matching_chars = 0
        sol_left, sol_right = None, None

        target = defaultdict(int)
        window = defaultdict(int)

        # count individual character frequency in t
        for c in t:
            target[c] += 1

        L = 0
        for R in range(len(s)):
            window[s[R]] += 1

            if s[R] in target and window[s[R]] <= target[s[R]]:
                matching_chars += 1

            while matching_chars == len(t):
                if sol_left is None and sol_right is None:
                    sol_left, sol_right = L, R
                elif R - L < sol_right - sol_left:
                    sol_left, sol_right = L, R

                if s[L] in target and window[s[L]] == target[s[L]]:
                    matching_chars -= 1
                window[s[L]] -= 1
                L += 1

        if sol_left is not None and sol_right is not None:
            return s[sol_left:sol_right + 1]
        else:
            return ""
