"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}

        curr = head
        while curr:
            if curr not in old_to_new:
                curr_node = Node(curr.val, None, None)
                old_to_new[curr] = curr_node
            else:
                curr_node = old_to_new[curr]
            
            if curr.next and curr.next not in old_to_new:
                new_next = Node(curr.next.val, None, None)
                old_to_new[curr.next] = new_next

                curr_node.next = new_next
            else:
                # .get used because None possible
                curr_node.next = old_to_new.get(curr.next)

            if curr.random and curr.random not in old_to_new:
                new_random = Node(curr.random.val, None, None)
                old_to_new[curr.random] = new_random

                curr_node.random = new_random
            else:
                curr_node.random = old_to_new.get(curr.random)
        
            curr = curr.next
        return old_to_new.get(head)