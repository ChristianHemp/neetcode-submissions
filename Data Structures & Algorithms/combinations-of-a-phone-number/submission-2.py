class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # hashmap for quick access to possible digit chars
        digit_to_chars = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        if len(digits) == 0:
            return []

        res = []

        def backtrack(index, curr_chars):
            if len(curr_chars) == len(digits):
                res.append(''.join(curr_chars))
                return
            
            # loop through every character and backtrack once char list reaches correct length
            for c in digit_to_chars[digits[index]]:
                curr_chars.append(c)
                backtrack(index + 1, curr_chars)
                curr_chars.pop()
        
        backtrack(0, [])
        return res
