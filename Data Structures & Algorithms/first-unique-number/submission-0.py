from collections import defaultdict

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = deque()
        self.counts = defaultdict(int)

        for num in nums:
            self.q.append(num)
            self.counts[num] += 1

    def showFirstUnique(self) -> int:
        while self.q and self.counts[self.q[0]] > 1:
            self.q.popleft()
        
        return self.q[0] if self.q else -1

    def add(self, value: int) -> None:
        self.q.append(value)
        self.counts[value] += 1


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
