class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0
        
        left = 0
        right = len(height) - 1
        water_level_left = height[left]
        water_level_right = height[right]
        res = 0

        while left < right:
            # increment/decrement left/right based on which has highest pillar
            if water_level_left < water_level_right:
                left += 1
                water_level_left = max(water_level_left, height[left])
                # no negative additions since water_level_left updated prior
                res += water_level_left - height[left]
            else:
                right -= 1
                water_level_right = max(water_level_right, height[right])
                # no negative additions since water_level_right updated prior
                res += water_level_right - height[right]
        
        return res