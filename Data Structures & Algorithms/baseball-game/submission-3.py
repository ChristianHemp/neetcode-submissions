class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "+":
                new_num = stack[-1] + stack[-2]
                stack.append(new_num)
            elif op == "C":
                stack.pop()
            elif op == "D":
                new_num = stack[-1] * 2
                stack.append(new_num)
            else:
                stack.append(int(op))

        return sum(stack)
