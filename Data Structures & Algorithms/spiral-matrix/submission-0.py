class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        res = []
        size = len(matrix) * len(matrix[0])
        up, left = 0, 0
        down = len(matrix) - 1
        right = len(matrix[0]) - 1

        while len(res) < size:
            # right
            for col in range(left, right + 1):
                res.append(matrix[up][col])
            
            # down
            for row in range(up + 1, down + 1):
                res.append(matrix[row][right])

            # left
            if up != down:
                for col in range(right - 1, left - 1, -1):
                    res.append(matrix[down][col])
            
            # up
            if left != right:
                for row in range(down - 1, up, -1):
                    res.append(matrix[row][left])
            
            left += 1
            right -= 1
            up += 1
            down -= 1
        
        return res