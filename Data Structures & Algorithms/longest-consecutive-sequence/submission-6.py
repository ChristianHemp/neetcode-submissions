class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        values = set(nums)
        longest = 1
        
        for num in nums:
            if num - 1 in values:
                continue
            
            length = 1
            while num + length in values:
                length += 1
            
            longest = max(longest, length)
        
        return longest
            

        
