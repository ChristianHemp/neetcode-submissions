# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head

        first = dummy
        second = dummy

        # traverse first pointer n+1 times so gap between first and second is n
        for i in range(n + 1):
            first = first.next
        
        # traverse both pointers still first is None
        while first:
            first = first.next
            second = second.next
        
        # second pointer will be at 1 before removal index
        second.next = second.next.next
        return dummy.next