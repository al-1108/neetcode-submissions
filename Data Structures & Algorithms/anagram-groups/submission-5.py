class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        seen = {}
        for i, str in enumerate(strs):
            count = [0] * 26
            for char in str:
                index = ord(char) - ord('a')
                count[index] += 1
            key = tuple(count)
            if key in seen:
                seen[key].append(i)
            else:
                seen[key] = [i]
        grouped = [[] for _ in range(len(seen))] 
        for i, key in enumerate(seen):
            for item in seen[key]:
                grouped[i].append(strs[item])
        return grouped