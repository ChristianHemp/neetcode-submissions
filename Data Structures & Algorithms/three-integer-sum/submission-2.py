class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        # iterate through sorted nums to pick all unique starting values
        for i in range(len(nums)):
            # skip over duplicate starting values
            if i != 0 and nums[i - 1] == nums[i]:
                continue

            # use left and right pointers to scan values to the right of start value
            left, right = i + 1, len(nums) - 1

            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                # combination found
                if curr_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                # sum too small
                elif curr_sum < 0:
                    left += 1
                # sum too large
                else:
                    right -= 1
        
        return result

