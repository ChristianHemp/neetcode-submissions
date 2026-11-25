# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sentinel = ListNode()
        sentinel.next = head

        first, second = sentinel, sentinel

        # traverse second ptr n + 1
        for _ in range(n + 1):
            second = second.next
        
        # traverse so that first ptr at n + 1 node from end of linked list
        while second:
            first = first.next
            second = second.next
        
        first.next = first.next.next
        return sentinel.next