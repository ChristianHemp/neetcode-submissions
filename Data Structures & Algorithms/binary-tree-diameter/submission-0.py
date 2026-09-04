# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0
        def dfs(root):
            nonlocal diameter

            if root is None:
                return -1
            
            length_left = dfs(root.left)
            length_right = dfs(root.right)

            diameter = max(diameter, length_left + length_right + 2)

            return max(length_left, length_right) + 1
        
        dfs(root)
        return diameter