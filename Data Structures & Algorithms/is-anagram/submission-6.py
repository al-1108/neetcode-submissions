class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen_s = {}
        for char in s:
            if char in seen_s:
                seen_s[char] += 1
            else:
                seen_s[char] = 1
        for char in t:
            if char in seen_s:
                seen_s[char] -= 1
                if seen_s[char] == 0:
                    del seen_s[char]
            else:
                return False
        return not seen_s
        
        