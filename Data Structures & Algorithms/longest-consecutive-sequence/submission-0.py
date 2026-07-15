class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                continue
            seen.add(num)
        possible_start = []
        for num in seen:
            if num-1 not in seen:
                possible_start.append(num)
        longest_consecutive = 0
        for num in possible_start:
            counter = 1
            while num+1 in seen:
                counter += 1
                num += 1
            if counter > longest_consecutive:
                longest_consecutive = counter
        return longest_consecutive