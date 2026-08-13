class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0

        for i in range(len(operations)):
            if operations[i] == "+":
                new_num = stack[-1] + stack[-2]
                stack.append(new_num)
            elif operations[i] == "C":
                stack.pop()
            elif operations[i] == "D":
                new_num = stack[-1] * 2
                stack.append(new_num)
            else:
                stack.append(int(operations[i]))

        return sum(stack)
