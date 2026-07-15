class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen = set(nums)
        longest_consecutive = 0
        for num in seen:
            if num-1 not in seen:
                counter = 1
                while num+1 in seen:
                    counter += 1
                    num += 1
                if counter > longest_consecutive:
                    longest_consecutive = counter
        return longest_consecutive