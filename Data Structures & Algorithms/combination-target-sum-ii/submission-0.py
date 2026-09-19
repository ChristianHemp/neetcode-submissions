class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()

        def backtrack(index, curr_sum, curr_values):
            if curr_sum == target:
                res.append(curr_values[:])
                return
            
            if curr_sum > target or index >= len(candidates):
                return
            
            # with value at i
            curr_values.append(candidates[index])
            backtrack(index + 1, curr_sum + candidates[index], curr_values)

            # without value at i (exclude repeat value elements)
            curr_values.pop()
            # skip copy elements since array sorted
            while index < len(candidates) - 1 and candidates[index] == candidates[index + 1]:
                index += 1
            backtrack(index + 1, curr_sum, curr_values)

        backtrack(0, 0, [])
        return res
