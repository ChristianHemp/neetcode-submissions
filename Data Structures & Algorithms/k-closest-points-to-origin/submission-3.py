class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        res = []

        for point in points:
            distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
            heapq.heappush(minHeap, [distance, point])
        
        for _ in range(k):
            res.append(heapq.heappop(minHeap)[1])
        
        return res