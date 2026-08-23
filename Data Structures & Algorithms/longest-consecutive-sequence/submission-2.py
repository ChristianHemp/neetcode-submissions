class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        heapq.heapify(nums)

        longest = 0
        k = 0
        prev = None
        while nums:
            curr = heapq.heappop(nums)
            if prev is not None:
                if curr == prev:
                    continue
                elif curr - 1 == prev:
                    k += 1
                else:
                    k = 1
            else:
                k += 1
            
            longest = max(longest, k)
            prev = curr

        return longest