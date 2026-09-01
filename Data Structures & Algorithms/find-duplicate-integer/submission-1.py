class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # Distance from start to beginning of cycle is always equal to distance of intersection of fast and slow to the beginning of cycle, start new pointer and increment both till intersection
        new_slow = 0
        while True:
            slow = nums[slow]
            new_slow = nums[new_slow]
            if new_slow == slow:
                return slow