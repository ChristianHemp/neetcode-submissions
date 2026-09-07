class MyQueue:

    def __init__(self):
        self.s1 = []    # bottom element front queue
        self.s2 = []    # top element front queue

    def push(self, x: int) -> None:
        if self.s1:
            self.s1.append(x)
        else:
            while len(self.s2) > 0:
                self.s1.append(self.s2.pop())
            
            self.s1.append(x)

    def pop(self) -> int:
        if self.s1:
            while len(self.s1) > 1:
                self.s2.append(self.s1.pop())
            
            return self.s1.pop()
        else:
            return self.s2.pop()


    def peek(self) -> int:
        if self.s1:
            return self.s1[0]
        elif self.s2:
            return self.s2[-1]
        else:
            return None

    def empty(self) -> bool:
        if len(self.s1) == 0 and len(self.s2) == 0:
            return True
        else:
            return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()