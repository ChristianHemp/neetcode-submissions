class Solution:
    def countElements(self, arr: List[int]) -> int:
        in_array = set(arr)

        count = 0
        for num in arr:
            if num + 1 in in_array:
                count += 1
        
        return count