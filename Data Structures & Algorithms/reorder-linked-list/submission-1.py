# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = head
        right = head

        # find middle index
        while right.next and right.next.next:
            mid = mid.next
            right = right.next.next
        
        temp = mid.next
        mid.next = None
        second = temp
        prev = None

        # reverse second half of linked list
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # alternate and merge both lists
        while prev:
            temp = head.next
            temp2 = prev.next

            head.next = prev
            prev.next = temp
            
            head = temp
            prev = temp2
