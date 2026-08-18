class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        self.heap.append(val)
        i = len(self.heap) - 1

        while i > 1 and self.heap[i] < self.heap[i // 2]:
            temp = self.heap[i]
            self.heap[i] = self.heap[i // 2]
            self.heap[i // 2] = temp
            i = i // 2

    def pop(self) -> int:
        if len(self.heap) == 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()
        
        res = self.heap[1]

        self.heap[1] = self.heap.pop()

        self.percolateDown(1)

        return res

    def top(self) -> int:
        if len(self.heap) > 1:
            return self.heap[1]
        else:
            return -1

    def heapify(self, nums: List[int]) -> None:
        if not nums:
            return None

        nums.append(nums[0])

        self.heap = nums
        curr = (len(self.heap) - 1) // 2
        
        while curr > 0:
            i = curr
            self.percolateDown(i)
            curr -= 1
    
    def percolateDown(self, i):
        while i * 2 < len(self.heap):
            if (i * 2 + 1 < len(self.heap) and
            self.heap[i * 2 + 1] < self.heap[i] and
            self.heap[i * 2 + 1] < self.heap[i * 2]):
                temp = self.heap[i]
                self.heap[i] = self.heap[i * 2 + 1]
                self.heap[i * 2 + 1] = temp
                i = i * 2 + 1
            elif self.heap[i * 2] < self.heap[i]:
                temp = self.heap[i]
                self.heap[i] = self.heap[i * 2]
                self.heap[i * 2] = temp
                i = i * 2
            else:
                break
        