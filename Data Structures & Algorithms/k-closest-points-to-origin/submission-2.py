class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        self.mergeSort(points)

        res = []

        for i in range(k):
            res.append(points[i])

        return res


    def mergeSort(self, arr):
        return self.mergeSortHelper(arr, 0, len(arr) - 1)


    def mergeSortHelper(self, arr, s, e):
        if e - s + 1 <= 1:
            return arr

        m = (s + e) // 2

        self.mergeSortHelper(arr, s, m)
        self.mergeSortHelper(arr, m + 1, e)

        self.merge(arr, s, m, e)

        return arr


    def merge(self, arr, s, m, e):
        left = arr[s:m + 1]
        right = arr[m + 1:e + 1]

        i = 0
        j = 0
        k = s

        while i < len(left) and j < len(right):
            if self.euclideanDist(left[i]) <= self.euclideanDist(right[j]):
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


    def euclideanDist(self, coords):
        return coords[0] ** 2 + coords[1] ** 2