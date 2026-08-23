class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0] * len(nums)
        suf = [0] * len(nums)
        res = []

        for i in range(len(nums)):
            if i == 0:
                pre[i] = 1
            else:
                pre[i] = nums[i - 1] * pre[i - 1]
        
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                suf[i] = 1
            else:
                suf[i] = nums[i + 1] * suf[i + 1]
        
        for i in range(len(nums)):
            res.append(pre[i] * suf[i])
            
        return res