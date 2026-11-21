class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        if not self.head:
            return True
        else:
            return False

    def append(self, value: int) -> None:
        newNode = Node(value)
        
        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        

    def appendleft(self, value: int) -> None:
        newNode = Node(value)

        if self.isEmpty():
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        
        if self.tail.prev:
            temp = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            return temp.val
        else:
            temp = self.tail
            self.head = self.tail = None
            return temp.val
        
    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        if self.head.next:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            return temp.val
        else:
            temp = self.head
            self.head = self.tail = None
            return temp.val
