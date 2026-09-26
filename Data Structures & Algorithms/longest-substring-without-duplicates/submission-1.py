class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0
        curr_length = 0

        left = 0
        for right in range(len(s)):
            if s[right] not in seen:
                seen.add(s[right])
                curr_length += 1
                longest = max(longest, curr_length)
            else:
                while s[left] != s[right]:
                    seen.remove(s[left])
                    curr_length -= 1
                    left += 1
                
                # move repeat char out of window, length not decremented since still "adding" s[right] to seen
                left += 1
        
        return longest