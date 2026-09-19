class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # simulate a decision tree

        # base case: when target == curr_val
        # base case 2: when curr_val > target: return 
        # .pop() when backtracking

        res = []

        def dfs(index, curr_value, curr_list):
            # Valid combination found
            if curr_value == target:
                res.append(curr_list[:])
                return
            
            # Values in current elements exceeds target
            if index >= len(nums) or curr_value > target:
                return

            # Try adding same value
            curr_list.append(nums[index])
            dfs(index, curr_value + nums[index], curr_list)

            # Try adding next index value
            curr_list.pop()
            dfs(index + 1, curr_value, curr_list)
        
        dfs(0, 0, [])
        return res
            

