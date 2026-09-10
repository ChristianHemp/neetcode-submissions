from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        char_counts = defaultdict(int)
        for c in s1:
            char_counts[c] += 1

        L = 0
        remaining_chars = len(s1)

        for R in range(len(s2)):
            if s2[R] not in char_counts:
                while L < R:
                    if s2[L] in char_counts:
                        char_counts[s2[L]] += 1
                        remaining_chars += 1
                    L += 1

                L = R + 1

            else:
                if char_counts[s2[R]] > 0:
                    char_counts[s2[R]] -= 1
                    remaining_chars -= 1

                    if remaining_chars == 0:
                        return True

                else:
                    while s2[L] != s2[R]:
                        if s2[L] in char_counts:
                            char_counts[s2[L]] += 1
                            remaining_chars += 1
                        L += 1

                    char_counts[s2[L]] += 1
                    remaining_chars += 1
                    L += 1

                    char_counts[s2[R]] -= 1
                    remaining_chars -= 1

            if R - L + 1 >= len(s1):
                if s2[L] in char_counts:
                    char_counts[s2[L]] += 1
                    remaining_chars += 1
                L += 1

        return False