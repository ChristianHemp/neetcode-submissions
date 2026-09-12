class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        
        res = []
        pq = []

        # pre-load first k - 1 values to heap
        for i in range(k - 1):
            heapq.heappush(pq, (-nums[i], i))
        
        L = 0
        for R in range(k - 1, len(nums)):
            heapq.heappush(pq, (-nums[R], R))

            res.append(-pq[0][0])

            L += 1

            # remove old indicies from root of heap
            while pq[0][1] < L:
                heapq.heappop(pq)
        
        return res
