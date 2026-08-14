class BrowserHistory:

    def __init__(self, homepage: str):
        self.prev_stack = []
        self.next_stack = []
        self.curr = homepage

    def visit(self, url: str) -> None:
        self.prev_stack.append(self.curr)
        self.curr = url
        self.next_stack.clear()

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.prev_stack:
                temp = self.prev_stack.pop()
                self.next_stack.append(self.curr)
                self.curr = temp
        
        return self.curr

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.next_stack:
                temp = self.next_stack.pop()
                self.prev_stack.append(self.curr)
                self.curr = temp
        
        return self.curr


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)