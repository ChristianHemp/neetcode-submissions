class Solution:
    def sortColors(self, nums: List[int]) -> None:
        buckets = [0, 0, 0]

        for i in nums:
            buckets[i] += 1
        
        i = 0
        for j in range(len(buckets)):
            for k in range(buckets[j]):
                nums[i] = j
                i += 1
        
        