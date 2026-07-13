class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        output = [1] * len(nums)
        prefix = 1
        suffix = 1
        for i in range(len(nums)):
            output[i] *= prefix
            prefix *= nums[i]
        for j in range(len(nums) -1, -1, -1):
            output[j] *= suffix
            suffix *= nums[j]
        return output