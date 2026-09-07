class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums)

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left_arr = arr[:mid]
        right_arr = arr[mid:]

        left_arr = self.merge_sort(left_arr)
        right_arr = self.merge_sort(right_arr)

        return self.merge(left_arr, right_arr)
    
    def merge(self, left_arr, right_arr):
        i, j = 0, 0

        merged_arr = []

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] <= right_arr[j]:
                merged_arr.append(left_arr[i])
                i += 1
            else:
                merged_arr.append(right_arr[j])
                j += 1
        
        while i < len(left_arr):
            merged_arr.append(left_arr[i])
            i += 1

        while j < len(right_arr):
            merged_arr.append(right_arr[j])
            j += 1
        
        return merged_arr