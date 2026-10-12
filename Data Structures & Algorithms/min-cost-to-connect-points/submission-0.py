class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        heap = [(0, 0)]
        included = [False] * n
        total_cost = 0
        edges_used = 0

        while edges_used < n:
            # pop min element from heap
            weight, curr_node = heapq.heappop(heap)

            # skip if already added
            if included[curr_node]:
                continue
            
            # mark as seen
            included[curr_node] = True
            total_cost += weight
            edges_used += 1

            # add all non-seen points as potential neighbors
            for new_node in range(n):
                if not included[new_node]:
                    new_weight = (
                        abs(points[curr_node][0] - points[new_node][0]) + abs(points[curr_node][1] - points[new_node][1])
                        ) 
                    
                    heapq.heappush(heap, (new_weight, new_node))

        return total_cost