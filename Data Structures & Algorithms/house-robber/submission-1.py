class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)

        if length == 1:
            return nums[0]
        elif length <= 2:
            return max(nums[0], nums[1])
        
        # initialize dp array
        dp = [0] * length
        dp[0], dp[1] = nums[0], nums[1]

        i = 2
        # 2 choices: 1 - rob house, 2 - skip house
        while i < length:
            # default case 1
            dp[i] = dp[i - 2] + nums[i]
            
            # maintains order for choice 2
            if dp[i - 2] > dp[i - 1]:
                dp[i - 1] = dp[i - 2]
    
            i += 1

        return max(dp[-1], dp[-2])
