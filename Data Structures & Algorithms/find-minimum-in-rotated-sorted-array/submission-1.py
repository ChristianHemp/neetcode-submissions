class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        left, right = 0, len(nums) - 1

        # case 1: no rotations
        if nums[left] < nums[right]:
            return nums[left]

        while left <= right:
            mid = (left + right) // 2

            # beginning of original array found
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            elif nums[mid] < nums[mid - 1]:
                return nums[mid]

            # remove impossible indices
            if nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1

        """
        [1,2,3,4,5,6]
        [3,4,5,6,1,2]
        [2,3,4,5,6,1]
        [4, 5, 6, 1, 2, 3]
        """

