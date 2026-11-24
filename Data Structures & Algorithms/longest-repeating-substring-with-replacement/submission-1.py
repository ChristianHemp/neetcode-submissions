from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_counts = defaultdict(int)    # char counts for current window
        result = 0

        left = 0
        highest_freq = 0    # tentative highest frequency char found
        for right in range(len(s)):
            window_counts[s[right]] += 1
            highest_freq = max(highest_freq, window_counts[s[right]])
            
            # remove leftmost element if window too large
            if (self.window_size(left, right)) - highest_freq > k:
                window_counts[s[left]] -= 1
                left += 1
            
            result = max(result, self.window_size(left, right))
        
        return result
    
    def window_size(self, left: int, right: int) -> int:
        return right - left + 1