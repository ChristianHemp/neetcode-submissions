class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 1:
            return 0
        
        result = 0
        left, right = 0, len(height) - 1
        left_water_level, right_water_level = height[left], height[right]

        while left < right:
            if left_water_level < right_water_level:
                left += 1
                left_water_level = max(left_water_level, height[left])
                result += left_water_level - height[left]
            else:
                right -= 1
                right_water_level = max(right_water_level, height[right])
                result += right_water_level - height[right]
        
        return result