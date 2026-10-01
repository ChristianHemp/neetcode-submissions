class Solution:
    def scoreOfString(self, s: str) -> int:
        score = 0
        for i in range(0, len(s) - 1):
            curr_score = abs(ord(s[i + 1]) - ord(s[i]))

            score += curr_score

        return score
