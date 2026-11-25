# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists) > 1:
            merged_lists = []
            for index in range(0, len(lists), 2):
                # not last index of list
                if index + 1 < len(lists):
                    merged_lists.append(self.mergeTwoLists(lists[index], lists[index + 1]))
                # last index of list
                else:
                    merged_lists.append(lists[index])
            lists = merged_lists
        
        return lists[0]
    

    def mergeTwoLists(self, list1, list2):
        sentinel = ListNode()
        tail = sentinel

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return sentinel.next

    
    """
    [lista, listb, listc, listd, liste]


    [1, 4, 7]

    [2, 6, 10, 11, 12, 13, 14, 15, 16, ... , 10000000]
    """