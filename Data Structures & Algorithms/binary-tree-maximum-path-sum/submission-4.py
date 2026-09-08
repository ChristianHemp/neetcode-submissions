# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path_sum = float('-inf')

        def dfs(node):
            nonlocal max_path_sum
            
            if node is None:
                return 0
            
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            # calculate max sum without including parent nodes
            curr_max_sum = node.val

            if left_sum > 0:
                curr_max_sum += left_sum
            if right_sum > 0:
                curr_max_sum += right_sum
                
            max_path_sum = max(max_path_sum, curr_max_sum)
            
            # add subtree with larger path sum unless both non-positive
            if left_sum > 0 or right_sum > 0:
                return max(node.val + left_sum, node.val + right_sum)
            else:
                return node.val
        
        dfs(root)
        return max_path_sum
