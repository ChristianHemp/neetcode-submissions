class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [0] * len(nums)
        suffixes = [0] * len(nums)
        result = []

        for i in range(len(nums)):
            if i == 0:
                prefixes[i] = 1
            else:
                prefixes[i] = nums[i - 1] * prefixes[i - 1]
        
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                suffixes[i] = 1
            else:
                suffixes[i] = nums[i + 1] * suffixes[i + 1]
        
        for i in range(len(nums)):
            result.append(prefixes[i] * suffixes[i])
        
        return result