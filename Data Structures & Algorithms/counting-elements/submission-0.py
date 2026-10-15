class Solution:
    def countElements(self, arr: List[int]) -> int:
        in_array = set()

        for num in arr:
            in_array.add(num)
        
        count = 0
        for num in arr:
            if num + 1 in in_array:
                count += 1
        
        return count