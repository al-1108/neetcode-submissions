class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        slow = slow2 = fast = 0
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            if slow == fast:
                break
        while True:
            slow, slow2 = nums[slow], nums[slow2]
            if slow == slow2:
                break
        return slow
        
        