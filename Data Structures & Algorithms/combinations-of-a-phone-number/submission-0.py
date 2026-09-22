class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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

        def backtrack(index, curr_str):
            if len(curr_str) == len(digits):
                res.append(curr_str)
                return
            
            for c in digit_to_chars[digits[index]]:
                curr_str += c
                backtrack(index + 1, curr_str)
                curr_str = curr_str[:-1]
        
        backtrack(0, '')
        return res
            
