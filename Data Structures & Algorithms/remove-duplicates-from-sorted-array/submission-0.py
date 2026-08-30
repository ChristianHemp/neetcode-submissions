class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        
        left = 0
        right = 1

        while right < len(nums):
            while right < len(nums) and nums[left] == nums[right]:
                nums.pop(right)
            left += 1
            right += 1

        return len(nums)