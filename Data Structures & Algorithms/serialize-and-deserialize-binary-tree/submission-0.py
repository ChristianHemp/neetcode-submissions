# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        strs = []

        def dfs(node):
            if node is None:
                strs.append("null")
                return

            strs.append(str(node.val))

            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return '%'.join(strs)
            


    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        strs = data.split('%')
        index = 0

        def dfs():
            nonlocal index

            if strs[index] == 'null':
                index += 1
                return None
            
            node = TreeNode(int(strs[index]))
            index += 1

            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()
