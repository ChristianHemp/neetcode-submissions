# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        last = None

        if root:
            q.append(root)
            last = root


        while len(q) > 0:
            for _ in range(len(q)):
                curr = q.popleft()

                if curr == last:
                    res.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if q:
                last = q[-1]
        return res
