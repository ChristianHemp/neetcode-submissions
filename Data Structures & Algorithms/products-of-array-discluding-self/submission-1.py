class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1
        zero_count = 0

        for num in nums:
            if num != 0:
                total_product *= num
            else:
                zero_count += 1
        
        result = [0] * len(nums)
        
        if zero_count >= 2:
            return result

        for i in range(len(nums)):
            if nums[i] != 0 and zero_count > 0:
                result[i] = 0
            elif nums[i] == 0 and zero_count > 0:
                result[i] = total_product
            else:
                result[i] = int(total_product / nums[i])

        return result