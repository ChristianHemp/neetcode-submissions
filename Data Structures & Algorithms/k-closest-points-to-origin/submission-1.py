import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        self.quickSort(points, 0, len(points) - 1)

        for i in range(k):
            res.append(points[i])
        
        return res

    def quickSort(self, arr, s, e):
        if e - s + 1 <= 1:
            return arr
        
        pivot = arr[e]
        left = s

        for i in range(s, e):
            if self.euclideanDist(arr[i]) < self.euclideanDist(pivot):
                temp = arr[left]
                arr[left] = arr[i]
                arr[i] = temp
                left += 1
        
        arr[e] = arr[left]
        arr[left] = pivot

        self.quickSort(arr, s, left - 1)
        self.quickSort(arr, left + 1, e)

        return arr
    
    def euclideanDist(self, coords: List[int]) -> int:
        return math.sqrt((coords[0] - 0) ** 2 + (coords[1] - 0) ** 2)


