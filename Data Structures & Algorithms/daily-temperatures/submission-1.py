class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = []
        output = [0] * len(temperatures)
        for i, num in enumerate(temperatures):
            while stack and (num > stack[-1][0]):
                count = i-stack[-1][1]
                output[stack[-1][1]] = count
                stack.pop()
            stack.append([num, i])
        return output