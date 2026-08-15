# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)

    def mergeSortHelper(self, arr, s, e):
        if e - s + 1 <= 1:
            return arr
        
        m = (s + e) // 2

        self.mergeSortHelper(arr, s, m)
        self.mergeSortHelper(arr, m + 1, e)

        self.merge(arr, s, m, e)

        return arr

    def merge(self, arr, s, m, e):
        left = arr[s : m + 1]
        right = arr[m + 1 : e + 1]

        i = 0   # left index
        j = 0   # right index
        k = s   # arr index

        while i < len(left) and j < len(right):
            if left[i].key <= right[j].key:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            
        while i < len(left):
            arr[k] = left[i]
            k += 1
            i += 1
            
        while j < len(right):
            arr[k] = right[j]
            k += 1
            j += 1
