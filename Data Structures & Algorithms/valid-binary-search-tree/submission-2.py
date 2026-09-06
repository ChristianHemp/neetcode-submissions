# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
    
        valid = True

        # Use inorder traversal
        def dfs(node, low, high):
            nonlocal valid

            if not node:
                return
            
            if not valid:
                return

            if node.val <= low or node.val >= high:
                valid = False

            dfs(node.left, low, node.val)
            dfs(node.right, node.val, high)
        
        dfs(root, float('-inf'), float('inf'))
        return valid
