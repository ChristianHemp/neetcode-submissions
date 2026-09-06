# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = 0
        path_max = root.val

        def dfs(node, path_max):
            nonlocal res

            if node is None:
                return
            
            if node.val >= path_max:
                res += 1
                path_max = node.val

            dfs(node.left, path_max)
            dfs(node.right, path_max)

        
        dfs(root, path_max)
        return res
