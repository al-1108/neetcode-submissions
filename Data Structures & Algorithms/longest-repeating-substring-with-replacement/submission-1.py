class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = set()
        highest = 0
        for char in s:
            if char not in seen:
                seen.add(char)
        
        for char in seen:
            count, l = 0, 0
            for r in range(len(s)):
                if s[r] == char:
                    count += 1
                while (r-l+1) - count > k:
                    if s[l] == char:
                        count -= 1
                    l += 1
                highest = max(highest, r-l+1)
        return highest


            
            



        