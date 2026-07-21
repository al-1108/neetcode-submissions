class Solution:
    def trap(self, height: list[int]) -> int:
        area = 0 
        current_trap_height = 0
        max_trap_height = 0
        l, r = 0, len(height)-1
        while l < r:
            current_trap_height = min(height[l], height[r])
            max_trap_height = max(current_trap_height, max_trap_height)
            if height[l] <= height[r]:
                l += 1
                if height[l] < max_trap_height:
                    area += max_trap_height-height[l]
            else:
                if height[r] < max_trap_height:
                    area += max_trap_height-height[r]
                r -= 1
        return area