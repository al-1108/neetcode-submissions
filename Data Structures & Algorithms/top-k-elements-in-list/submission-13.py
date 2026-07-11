class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        seen = {}
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1
        frequency = [[] for _ in range(len(nums)+1)]
        for key in seen:
            frequency[seen[key]].append(key)
        count = 0 
        top_frequent = []
        for i in range(len(frequency) - 1, -1, -1):
            for item in frequency[i]: 
                top_frequent.append(item)
                count += 1
                if count == k:
                    return top_frequent