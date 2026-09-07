class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        sorted_arr = []

        while nums:
            sorted_arr.append(heapq.heappop(nums))
        
        return sorted_arr