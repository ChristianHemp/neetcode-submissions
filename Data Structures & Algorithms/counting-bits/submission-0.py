class Solution:
    def countBits(self, n: int) -> List[int]:
        count = 0
        res = [0]

        for i in range(1, n + 1):
            while i > 0:
                if i & 1 == 1:
                    count += 1
            
                i = i >> 1

            res.append(count)
            count = 0

        return res