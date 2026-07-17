class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j, k = i+1, len(nums)-1
            total = nums[i] + nums[j] + nums[k]
            while j < k:
                if (j < k and total < 0) or j == i:
                    j += 1
                if (j < k and total > 0) or k == i:
                    k -= 1
                total = nums[i] + nums[j] + nums[k]
                if total == 0 and j != k != i:
                    triplet = [nums[i], nums[j], nums[k]]
                    triplets.append(triplet)
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
        return triplets