class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        row = None

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                row = mid
                break

            if target < matrix[mid][0]:
                right = mid - 1
            elif target > matrix[mid][0]:
                left = mid + 1
            else:
                return True

        if row is None:
            return False

        left = 0
        right = len(matrix[row]) - 1

        while left <= right:
            mid = (left + right) // 2

            if target < matrix[row][mid]:
                right = mid - 1
            elif target > matrix[row][mid]:
                left = mid + 1
            else:
                return True
        
        return False

            
            