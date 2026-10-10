from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = defaultdict(int)
        count = 0
        valid = {'b', 'a', 'l', 'o', 'n'}
        s = "balloon"

        for c in text:
            if c in valid:
                counts[c] += 1
        
        while True:
            for c in s:
                counts[c] -= 1

                if counts[c] < 0:
                    return count
            count += 1