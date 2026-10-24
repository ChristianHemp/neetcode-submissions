class Solution:
    def reverseBits(self, n: int) -> int:
        result = []

        for i in range(32):
            if n & (1 << i):
                result.append("1")
            else:
                result.append("0")
        
        return int(''.join(result), 2)  # returns binary format of resulting string