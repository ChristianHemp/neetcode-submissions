class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        
        is_increasing = None

        for i in range(len(nums) - 1):
            if is_increasing is None:
                if nums[i] != nums[i + 1]:
                    is_increasing = True if nums[i + 1] > nums[i] else False

            if is_increasing and nums[i] > nums[i + 1]:
                return False
            elif not is_increasing and nums[i] < nums[i + 1]:
                return False
        
        return True