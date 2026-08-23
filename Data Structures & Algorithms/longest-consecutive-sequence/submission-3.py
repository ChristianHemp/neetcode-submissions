class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        k = 1

        for num in nums:
            if num - 1 in num_set:
                continue
            
            while num + 1 in num_set:
                k += 1
                num += 1
            
            longest = max(k, longest)
            k = 1

        return longest