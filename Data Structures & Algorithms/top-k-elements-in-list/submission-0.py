from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            counts[num] += 1
        
        for key, val in counts.items():
            freq[val].append(key)
        
        res = []

        for i in range(len(freq) - 1, 0, -1):
            for element in freq[i]:
                res.append(element)
                if len(res) == k:
                    return res
