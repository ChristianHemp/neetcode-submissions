class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum, curr_sum = nums[0], 0

        for num in nums:
            curr_sum = max(curr_sum + num, num) # only keep previous sum if positive
            max_sum = max(max_sum, curr_sum)
        
        return max_sum