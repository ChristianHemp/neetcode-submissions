class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}

        for index in range(len(nums)):
            complement = target - nums[index]

            if complement in complements:
                return [complements[complement], index]

            complements[nums[index]] = index
            