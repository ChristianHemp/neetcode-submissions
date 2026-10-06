class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = s.strip()
        length = len(string) - 1
        i = length

        while i >= 0:
            if string[i] == ' ':
                return length - i
            else:
                i -= 1
        
        return len(string)