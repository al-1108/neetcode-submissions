class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        highest = 0
        stack = []
        heights.append(0)
        for i, h in enumerate(heights):
            start = i
            while stack and (h < stack[-1][0]):
                height, index = stack.pop()
                highest = max(highest, height*(i-index))
                start = index
            stack.append([h, start])
        return highest