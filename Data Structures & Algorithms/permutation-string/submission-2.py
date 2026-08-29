class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen = {}
        for c in s1:
            if c in seen:
                seen[c] += 1
            else:
                seen[c] = 1
        seen2 = {}
        l = 0
        for r in range(len(s2)):
            if s2[r] in seen2:
                seen2[s2[r]] += 1
            else:
                seen2[s2[r]] = 1
            if len(s1) < (r-l+1):
                seen2[s2[l]] -= 1
                if seen2[s2[l]] == 0:
                    del seen2[s2[l]]
                l += 1
            
            if seen == seen2:
                return True
        return False


        