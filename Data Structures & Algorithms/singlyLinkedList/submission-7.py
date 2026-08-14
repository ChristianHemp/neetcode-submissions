class Node:

    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int:
        curr = self.head

        for i in range(index):
            if curr is None:
                return -1
            curr = curr.next
        
        if curr is None:
            return -1

        return curr.val
            

    def insertHead(self, val: int) -> None:
        if self.head is None:
            new_node = Node(val)
            self.head = new_node
            self.tail = new_node
            return
        
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def insertTail(self, val: int) -> None:
        if self.head is None:
            new_node = Node(val)
            self.head = new_node
            self.tail = new_node
            return
        
        new_node = Node(val)
        self.tail.next = new_node
        self.tail = new_node

    def remove(self, index: int) -> bool:
        i = 0
        curr = self.head

        if index == 0 and curr and curr.next:
            self.head = curr.next
            return True
        elif index == 0 and curr:
            self.head = None
            self.tail = None
            return True

        while i < index - 1 and curr:
            i += 1
            curr = curr.next
        
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next
            return True
        else:
            return False

    def getValues(self) -> List[int]:
        arr = []
        curr = self.head
        while curr != None:
            arr.append(curr.val)
            curr = curr.next
        
        return arr
