class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        longest = 0
        left = 0

        for right in range(len(s)):
            if s[right] in seen:
                longest = max(longest, len(seen))

                while s[left] != s[right] and s[left] in seen:
                    seen.remove(s[left])
                    left += 1
                
                left += 1
            else:
                seen.add(s[right])
        
        longest = max(longest, len(seen))
        return longest