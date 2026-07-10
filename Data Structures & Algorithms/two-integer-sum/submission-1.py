class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if target-num in seen:
                j = i
                i = seen[target-num]
                break
            if num in seen:
                continue
            seen[num] = i
        return [i, j]