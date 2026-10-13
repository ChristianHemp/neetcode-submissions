class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        possible = set(range(1, len(nums) + 1))

        for num in nums:
            possible.discard(num)
        
        return list(possible)