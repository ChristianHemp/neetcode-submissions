from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)
        threshold = len(nums) // 3
        result = []

        for num in nums:
            counts[num] += 1

        for key, value in counts.items():
            if value > threshold:
                result.append(key)
        
        return result