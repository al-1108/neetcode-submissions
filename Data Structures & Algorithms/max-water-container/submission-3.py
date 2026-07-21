class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l, r = 0, len(heights)-1
        highest = 0
        while l < r:
            area = (r-l)*min(heights[l], heights[r])
            highest = max(highest, area)
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        return highest