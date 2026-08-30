class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        next_new_index = 0
        prev = None
        
        for num in nums:
            if num == prev:
                continue
            nums[next_new_index] = num
            prev = num
            next_new_index += 1
        
        return next_new_index