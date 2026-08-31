class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r, output = 0, 0, []
        window = deque()
        while r < k-1:
            while window and nums[window[-1]] < nums[r]:
                window.pop()
            window.append(r)
            r += 1
        while r < len(nums):
            while window and nums[window[-1]] < nums[r]:
                window.pop()
            window.append(r)
            if l > window[0]:
                window.popleft()
            output.append(nums[window[0]])
            l, r = l + 1, r + 1
        return output        