from collections import defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = defaultdict(int)

        for task in tasks:
            counts[task] += 1
        
        heap = [-val for val in counts.values()]
        heapq.heapify(heap)

        q = deque()
        time = 0

        while heap or q:
            time += 1

            if heap:
                count = heapq.heappop(heap) + 1

                if count < 0:
                    q.append((time + n, count))
            
            if q and q[0][0] == time:
                _, count = q.popleft()
                heapq.heappush(heap, count)
        
        return time