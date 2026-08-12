class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        next_max = 0
        for i in range(len(arr) - 1):
            next_max = 0
            for j in range(i + 1, len(arr)):
                if arr[j] > next_max:
                    next_max = arr[j]

            arr[i] = next_max
        
        arr[-1] = -1
        return arr