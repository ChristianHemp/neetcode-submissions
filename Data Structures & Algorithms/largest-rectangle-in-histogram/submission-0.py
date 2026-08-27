class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        largest = 0
        stack = []

        # Use ordered pair to determine length of each rectangle
        for i, height in enumerate(heights):
            rect_start = i  # used to calculate width (index - start)
            # pop all rectangles too large to continue
            while stack and height < stack[-1][1]:
                start_index, curr_height = stack.pop()
                largest = max(largest, curr_height * (i - start_index))
                # new rectangle "starts" at leftmost possible point
                rect_start = start_index
            stack.append((rect_start, height))
        
        # remaining values in stack calculated
        for rect_start, height in stack:
            largest = max(largest, height * (len(heights) - rect_start))
        
        return largest