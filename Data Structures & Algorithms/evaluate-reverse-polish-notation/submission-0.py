class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {'+', '-', '*', '/'}

        for token in tokens:
            if token not in operations:
                stack.append(int(token))
                continue

            num2 = stack.pop()  # right side of operation
            num1 = stack.pop()  # left side of operation

            if token == '+':
                res = num1 + num2
                stack.append(res)
            elif token == '-':
                res = num1 - num2
                stack.append(res)
            elif token == '*':
                res = num1 * num2
                stack.append(res)
            else:
                res = int(num1 / num2)  # python int() truncates towards 0
                stack.append(res)
        
        return stack.pop()