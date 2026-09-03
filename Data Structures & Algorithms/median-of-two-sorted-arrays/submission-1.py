class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr1, arr2 = nums1, nums2
        length = len(nums1) + len(nums2)
        half_length = length // 2

        if len(arr1) > len(arr2):
            arr1, arr2 = arr2, arr1
        
        left, right = 0, len(arr1) - 1

        while True:
            mid = (left + right) // 2
            mid2 = half_length - mid - 2
        
            arr1_left = arr1[mid] if mid >= 0 else float("-infinity")
            arr1_right= arr1[mid + 1] if (mid + 1) < len(arr1) else float("infinity")
            arr2_left = arr2[mid2] if mid2 >= 0 else float("-infinity")
            arr2_right = arr2[mid2 + 1] if (mid2 + 1) < len(arr2) else float("infinity")

            if arr1_left <= arr2_right and arr2_left <= arr1_right:
                if length % 2:
                    return min(arr1_right, arr2_right)
            
                return (max(arr1_left, arr2_left) + min(arr1_right, arr2_right)) / 2
            elif arr1_left > arr2_right:
                right = mid - 1
            else:
                left = mid + 1
        