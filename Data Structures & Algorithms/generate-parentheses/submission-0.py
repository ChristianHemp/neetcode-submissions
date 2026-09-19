class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []

        def backtrack(num_open, num_closed, curr_chars):
            # invalid string
            if num_open < num_closed or num_open > n:
                return
            
            # valid string found
            if len(curr_chars) == 2 * n:
                res.append(''.join(curr_chars))
                return
            
            # add new open bracket
            curr_chars.append('(')
            backtrack(num_open + 1, num_closed, curr_chars)
            curr_chars.pop()

            # add new closed bracket
            curr_chars.append(')')
            backtrack(num_open, num_closed + 1, curr_chars)
            curr_chars.pop()
        
        backtrack(0, 0, [])
        return res