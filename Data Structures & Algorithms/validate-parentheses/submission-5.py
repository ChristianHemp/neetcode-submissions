class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char == '(' or char == '[' or char == '{':
                stack.append(char)
            else:
                # check for empty stack to avoid error
                if not stack:
                    return False
                
                if char == ')' and stack.pop() != '(':
                    return False
                elif char == ']' and stack.pop() != '[':
                    return False
                elif char == '}' and stack.pop() != '{':
                    return False
        
        return len(stack) == 0