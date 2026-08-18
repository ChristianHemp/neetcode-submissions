class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            max_heap.append(stone * -1)
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            stone1 = -1 * heapq.heappop(max_heap)
            stone2 = -1 * heapq.heappop(max_heap)

            if stone1 == stone2:
                continue
            elif stone1 < stone2:
                stone2 -= stone1
                heapq.heappush(max_heap, -1 * stone2)
            else:
                stone1 -= stone2
                heapq.heappush(max_heap, -1 * stone1)
        
        if max_heap:
            return -1 * max_heap.pop()
        else:
            return 0
