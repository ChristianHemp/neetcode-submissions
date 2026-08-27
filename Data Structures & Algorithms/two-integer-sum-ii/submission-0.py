class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            left = i + 1
            right = len(numbers)
            while left <= right:
                mid = (right + left) // 2
                if mid < 0 or mid >= len(numbers):
                    break
                curr_sum = numbers[i] + numbers[mid]
                if curr_sum == target:
                    return [i + 1, mid + 1]
                elif curr_sum < target:
                    left = mid + 1
                else:
                    right = mid - 1