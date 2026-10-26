class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        if len(set(nums)) != len(nums):
            return False
        
        return True if max(nums) - min(nums) + 1 == len(nums) else False
