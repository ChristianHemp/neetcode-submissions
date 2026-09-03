# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root, height):
            if root is None:
                return 0
            
            height_left = 1 + dfs(root.left, height)
            height_right = 1 + dfs(root.right, height)

            return max(height_left, height_right)
        
        return dfs(root, 0)