class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        characters = set(s)
        longest = 0

        for char in characters:
            left = 0
            count = 0

            for right in range(len(s)):
                if s[right] == char:
                    count += 1
                
                while not self.valid_window(left, right, count, k):
                    if s[left] == char:
                        count -= 1
                    left += 1
                
                longest = max(longest, right - left + 1)
        
        return longest
    
    def valid_window(self, left, right, count, k):
        return right - left - count + 1 <= k