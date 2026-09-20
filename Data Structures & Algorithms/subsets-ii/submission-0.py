class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        subset = []

        def backtrack(index):
            if index >= len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[index])
            backtrack(index + 1)

            subset.pop()
            # Skip duplicate numbers (will be in order after sort)
            while index < len(nums) - 1 and nums[index] == nums[index + 1]:
                index += 1
                
            backtrack(index + 1)
        
        backtrack(0)
        return res