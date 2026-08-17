# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def hasPathSumHelper(root, curr_sum):
            if not root:
                return False
            
            curr_sum += root.val

            if not root.left and not root.right:
                return curr_sum == targetSum
            if hasPathSumHelper(root.left, curr_sum):
                return True
            if hasPathSumHelper(root.right, curr_sum):
                return True

            return False
        
        return hasPathSumHelper(root, 0)