class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b, 
            '*': lambda a, b: a * b, 
            '/': lambda a, b: int(a / b)
            }

        for token in tokens:
            if token not in operations:
                stack.append(int(token))
                continue

            num2 = stack.pop()  # right side of operation
            num1 = stack.pop()  # left side of operation
            operation = operations[token]
            stack.append(operation(num1, num2))

        return stack.pop()