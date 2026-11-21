class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum = 0
        left, right = 0, len(heights) - 1

        while left < right:
            # calculate area with current bars
            curr_area = min(heights[left], heights[right]) * (right - left)

            # update maximum if pertinent
            maximum = max(maximum, curr_area)

            # increment/decrement the smaller bar
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return maximum