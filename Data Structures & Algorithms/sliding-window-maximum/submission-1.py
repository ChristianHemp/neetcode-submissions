class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = deque()   # store indices of nums

        for R in range(len(nums)):
            # remove old indices from front of queue
            while q and q[0] <= R - k:
                q.popleft()
            
            # remove indicies with smaller values from back of queue
            while q and nums[q[-1]] <= nums[R]:
                q.pop()
            
            # add new index
            q.append(R)

            # add to result once sufficient window size reached
            if R >= k - 1:
                res.append(nums[q[0]])
        
        return res