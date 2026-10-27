class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 1
        num_set = set(nums)

        if len(nums) == 0:
            return 0

        for num in nums:
            if num - 1 in num_set:
                continue
            
            length = 1
            while num + length in num_set:
                length += 1
            
            longest = max(longest, length)
        return longest