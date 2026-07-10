class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]
            suffix[len(nums)-i-1] = suffix[len(nums)-i]*nums[len(nums)-i]
        for i in range(0, len(nums)):
            output.append(prefix[i]*suffix[i])
        return output



            
        