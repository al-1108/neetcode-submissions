class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for i, string in enumerate(strs):
            count = [0] * 26
            for char in string:
                index = ord(char) - ord("a")
                count[index] += 1
            if tuple(count) in seen:
                seen[tuple(count)].append(i)
            else:
                seen[tuple(count)] = [i]
        grouped_Anagrams = []
        for key in seen:
            anagrams = []
            for index in seen[key]:
                anagrams.append(strs[index])
            grouped_Anagrams.append(anagrams)
        return grouped_Anagrams





    
        