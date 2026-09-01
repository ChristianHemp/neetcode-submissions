# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        right = head
        mid = head

        while right.next and right.next.next:
            right = right.next.next
            mid = mid.next
        
        second = mid.next
        mid.next = None

        prev = None
        curr = second
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # reversed head at prev
        while prev:
            temp = head.next
            temp2 = prev.next

            head.next = prev
            prev.next = temp

            head = temp
            prev = temp2