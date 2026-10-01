from collections import defaultdict

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        frequency_map = defaultdict(int)

        for num in nums:
            frequency_map[num] += 1
        
        largest = -1

        for key, value in frequency_map.items():
            if value != 1:
                continue
            
            largest = max(largest, key)
        
        return largest