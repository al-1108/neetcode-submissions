class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen = set(nums)
        longest_consecutive = 0
        for num in seen:
            if num-1 not in seen:
                counter = 1
                while num+counter in seen:
                    counter += 1
                longest_consecutive = max(counter, longest_consecutive)
        return longest_consecutive