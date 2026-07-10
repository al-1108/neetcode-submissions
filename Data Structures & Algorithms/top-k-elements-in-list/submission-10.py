class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        for num in nums:
            seen[num] += 1
        # counts array of arrays
        # each index in counts array corresponds to the number of elements

        counts = [[] for _ in range(len(nums)+1)]
        for key in seen:
            counts[seen[key]].append(key)
        arr = []
        counter = 0
        for i in reversed(counts):
            for element in i:
                arr.append(element)
                counter += 1
                if counter == k:
                    return arr




        