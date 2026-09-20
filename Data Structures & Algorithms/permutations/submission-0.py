class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []

        def backtrack(curr, seen):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for num in nums:
                if num not in seen:
                    curr.append(num)
                    seen.add(num)

                    backtrack(curr, seen)

                    curr.pop()
                    seen.remove(num)
        
        backtrack([], set())
        return res