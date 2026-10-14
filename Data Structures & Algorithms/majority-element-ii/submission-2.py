class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate_a_count, candidate_b_count = 0, 0
        candidate_a, candidate_b = None, None

        for num in nums:
            if candidate_a == num:
                candidate_a_count += 1
            elif candidate_b == num:
                candidate_b_count += 1
            elif candidate_a_count == 0:
                candidate_a = num
                candidate_a_count += 1
            elif candidate_b_count == 0:
                candidate_b = num
                candidate_b_count += 1
            else:
                candidate_a_count -= 1
                candidate_b_count -= 1
        
        result = []
        threshold = len(nums) // 3

        if nums.count(candidate_a) > threshold:
            result.append(candidate_a)
        
        if nums.count(candidate_b) > threshold:
            result.append(candidate_b)
        
        return result