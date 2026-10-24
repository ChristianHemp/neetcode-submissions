class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        curr_count = 0

        for i in range(n + 1):
            # technically only need 17 bits since 2^17 > 10^5 (constraint), however, more standard to say 32 assuming 32 bit unsigned
            for j in range(32):
                if i & (1 << j):
                    curr_count += 1
            
            result.append(curr_count)
            curr_count = 0
        
        return result
