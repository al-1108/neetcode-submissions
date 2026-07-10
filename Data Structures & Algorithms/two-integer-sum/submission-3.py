class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            compliment = target-num
            if compliment in seen:
                compliment_index = seen[compliment]
                return [compliment_index, i]
            if num in seen:
                continue
            seen[num] = i