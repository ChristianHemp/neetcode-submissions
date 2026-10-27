class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            # push any open parenthesis to stack
            if char == '(' or char == '{' or char == '[':
                stack.append(char)
            else:
                # check for empty stack
                if not stack:
                    return False
                
                # check for matching opening parenthesis in stack
                popped = stack.pop()
                if char == ')' and popped != '(':
                    return False
                elif char == '}' and popped != '{':
                    return False
                elif char == ']' and popped != '[':
                    return False
            
        return len(stack) == 0