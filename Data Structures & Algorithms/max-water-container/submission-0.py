class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l, r = 0, len(heights)-1
        highest = (r-l)*min(heights[l], heights[r])
        while l < r:
            if heights[l] >= heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            area = (r-l)*min(heights[l], heights[r])
            if area > highest:
                highest = area
        return highest