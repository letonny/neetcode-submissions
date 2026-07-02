class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)

        result = [0] * n

        for i in range(n):
            
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev_temp = stack.pop()
                result[prev_temp] = i - prev_temp
            stack.append(i)
        
        return result