class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_chars = set()
        longest = 0
        left = 0
        
        for right in range(len(s)):
            # check for duplicate
            if s[right] in curr_chars:
                while s[left] != s[right]:
                    curr_chars.remove(s[left])
                    left += 1
                left += 1
            else:
                curr_chars.add(s[right]) # add new character to set
                longest = max(longest, len(curr_chars))
        
        return longest