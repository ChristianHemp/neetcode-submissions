class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, sublist, total):
            if total == target:
                res.append(sublist[:])
                return
            
            if i >= len(nums) or total > target:
                return
            
            sublist.append(nums[i])
            dfs(i, sublist, total + nums[i])

            sublist.pop()
            dfs(i + 1, sublist, total)
        
        dfs(0, [], 0)
        return res
            
