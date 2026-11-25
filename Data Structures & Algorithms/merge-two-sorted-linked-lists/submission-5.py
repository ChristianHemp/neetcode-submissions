# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a new linked list
        dummy_head = ListNode()
        tail = dummy_head

        # loop while list 1 and list 2 still have unused nodes, taking the smaller value node each time
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # append the rest of the linked list that has remaining valuse
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy_head.next

        # 1, 2, 4, 5 
        # 3, 10, 11, 12

        # DUMMY, 1, 2, 3, 4, 5, 

