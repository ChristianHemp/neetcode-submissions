# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        sublist = []
        q = deque()

        if root:
            q.append(root)
        
        while len(q) > 0:
            for _ in range(len(q)):
                curr = q.popleft()
                sublist.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(sublist[:])
            sublist.clear()
        
        return res
            