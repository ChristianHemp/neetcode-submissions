class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [len(temperatures) - 1]

        for i in range(len(temperatures) - 2, -1, -1):
            if temperatures[i] < temperatures[stack[-1]]:
                result[i] = stack[-1] - i
            else:
                while stack and temperatures[i] >= temperatures[stack[-1]]:
                    stack.pop()
                
                if stack:
                    result[i] = stack[-1] - i
                else:
                    result[i] = 0
            
            stack.append(i)
        
        return result