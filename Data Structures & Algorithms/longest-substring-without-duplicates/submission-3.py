class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_window = set()
        longest = 0

        left = 0
        for right in range(len(s)):
            if s[right] not in curr_window:
                curr_window.add(s[right])
                longest = max(longest, len(curr_window))
            else:
                while s[left] != s[right]:
                    curr_window.remove(s[left])
                    left += 1
                
                left += 1
        
        return longest