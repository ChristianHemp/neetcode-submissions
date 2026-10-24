class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        curr_window = set()
        
        left = 0
        for right in range(len(s)):
            if s[right] not in curr_window:
                curr_window.add(s[right])
            else:
                longest = max(len(curr_window), longest)
                while s[left] != s[right]:
                    curr_window.remove(s[left])
                    left += 1
                left += 1
        
        return max(longest, len(curr_window))