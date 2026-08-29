class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1

        if nums[right] > nums[left]:
            return nums[left]

        while left <= right:
            mid = (left + right) // 2

            if nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            elif nums[mid - 1] > nums[mid]:
                return nums[mid]
            
            if nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1
            
        return min_val