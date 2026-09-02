# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)

        carryover = 0
        curr = dummy
        while l1 != None or l2 != None or carryover != 0:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            res = num1 + num2 + carryover
            carryover = res // 10

            new_node = ListNode(res % 10)
            curr.next = new_node
            curr = new_node
            
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next