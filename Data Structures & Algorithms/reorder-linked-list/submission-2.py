# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # identify middle node of the linked list (fast and slow pointer)
        mid, fast = head, head
        while fast and fast.next:
            mid = mid.next
            fast = fast.next.next
        
        # reverse second half of linked list starting from middle node
        second = mid.next
        mid.next = None
        prev = None

        while second:
            temp = second.next
            second.next = prev
            prev = second   # prev will be head of reversed second half after process is done
            second = temp
        
        # merge first half and reversed second half values into finalized reordered list
        while prev:
            temp1 = head.next
            temp2 = prev.next

            head.next = prev
            prev.next = temp1

            head = temp1
            prev = temp2
