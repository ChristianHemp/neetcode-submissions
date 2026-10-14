from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)
        threshold = len(nums) // 3
        result = set()

        for num in nums:
            counts[num] += 1
            if counts[num] > threshold:
                result.add(num)

        return list(result)