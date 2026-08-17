# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def hasPathSumHelper(root, arr):
            if not root:
                return False
            
            arr.append(root.val)

            if not root.left and not root.right:
                if sum(arr) == targetSum:
                    return True
                arr.pop()
                return False
            if hasPathSumHelper(root.left, arr):
                return True
            if hasPathSumHelper(root.right, arr):
                return True
            
            arr.pop()
            return False
        
        arr = []
        return hasPathSumHelper(root, arr)