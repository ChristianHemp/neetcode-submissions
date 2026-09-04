# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def dfs(root, subRoot):
            if not root and not subRoot:
                return True
            
            if not root or not subRoot:
                return False
            
            if root.val != subRoot.val:
                return False

            return (
                dfs(root.left, subRoot.left) and
                dfs(root.right, subRoot.right)
                )

        if root.val == subRoot.val and dfs(root, subRoot):
            return True

        if dfs(root.right, subRoot) or dfs(root.left, subRoot):
            return True

        return (
            self.isSubtree(root.left, subRoot) or 
            self.isSubtree(root.right, subRoot)
            )
        