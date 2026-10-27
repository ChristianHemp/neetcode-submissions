class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: int(x / y)
        }

        for token in tokens:
            if token.lstrip('-').isnumeric():
                stack.append(token)
            else:
                # second value operates first for - and /
                val2 = int(stack.pop())
                val1 = int(stack.pop())
                operation = operations[token]
                stack.append(operation(val1, val2))
        
        return int(stack[0])

