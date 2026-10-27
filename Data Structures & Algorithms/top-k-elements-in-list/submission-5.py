class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        frequencies = [[] for _ in range(len(nums) + 1)]
        result = []

        for num in nums:
            counts[num] += 1
        
        for key, value in counts.items():
            frequencies[value].append(key)

        for i in range(len(frequencies) - 1, 0, -1):
            for num in frequencies[i]:
                result.append(num)
                if len(result) == k:
                    return result
        