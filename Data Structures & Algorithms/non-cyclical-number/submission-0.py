class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)
            numStr = str(n)
            n = 0
            for d in numStr:
                n += (int(d) ** 2)
            if n == 1:
                return True
        return False