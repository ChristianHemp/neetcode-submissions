class LLNode:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size or self.size == 0:
            return -1
        
        curr = self.head
        i = 0

        while i < index:
            if curr.next is None:
                return -1
            curr = curr.next
            i += 1
        
        return curr.val


    def addAtHead(self, val: int) -> None:
        if self.size == 0:
            self.head = LLNode(val)
            self.tail = self.head
            self.size += 1
            return
        
        new_node = LLNode(val)
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.size == 0:
            self.tail = LLNode(val)
            self.head = self.tail
            self.size += 1
            return
        
        new_node = LLNode(val)
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return None
        
        curr = self.head
        i = 0

        if index == 0:
            self.addAtHead(val)
            return

        while i < index - 1:
            if curr.next is None:
                return
            curr = curr.next
            i += 1
        
        new_node = LLNode(val)

        if curr.next is None:
            self.addAtTail(val)
            return

        new_node.next = curr.next
        new_node.next.prev = new_node
        curr.next = new_node
        new_node.prev = curr
        self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return None
        
        curr = self.head
        i = 0

        if self.head is None and self.tail is None:
            return

        if self.head == self.tail:
            self.head = None
            self.tail = None
            self.size -= 1
            return

        if index == 0:
            curr.next.prev = None
            self.head = curr.next
            self.size -= 1
            return

        while i < index:
            if curr.next is None:
                return
            curr = curr.next
            i += 1

        
        if curr.next is None:
            curr.prev.next = None
            self.tail = curr.prev
            self.size -= 1
            return

        curr.next.prev = curr.prev
        curr.prev.next = curr.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)