"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        original_to_cloned = {}

        def dfs(node):
            if node in original_to_cloned:
                return original_to_cloned[node]
            
            copy = Node(node.val)
            original_to_cloned[node] = copy

            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            
            return copy
        
        if node:
            return dfs(node)
        else:
            return None
