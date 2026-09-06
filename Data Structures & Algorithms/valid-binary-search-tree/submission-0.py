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
        
        max_heap = []
        valid = True

        # Use inorder traversal
        def inorder(node):
            nonlocal valid

            if node is None:
                return
            
            inorder(node.left)

            if not max_heap:
                heapq.heappush_max(max_heap, node.val)
            elif node.val <= max_heap[0]:
                valid = False
            else:
                heapq.heappush_max(max_heap, node.val)
            
            inorder(node.right)
        
        inorder(root)
        return valid
