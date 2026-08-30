class Solution:
    def minWindow(self, s: str, t: str) -> str:
        seen = {}
        for char in t:
            if char not in seen:
                seen[char] = 1
            else:
                seen[char] += 1
        need = len(seen)
        have = 0
        l = 0
        seen2 = {}
        window_length = 100001 # constraint max length 100k
        splice = []
        for r in range(len(s)):
            if s[r] in seen:
                if s[r] in seen2:
                    seen2[s[r]] += 1
                else:
                    seen2[s[r]] = 1
                if seen2[s[r]] == seen[s[r]]:
                    have += 1

            while have == need:
                if window_length > (r-l+1):
                    window_length = r-l+1
                    splice = [l, r]
                
                if s[l] in seen2:
                    seen2[s[l]] -= 1
                    if seen2[s[l]] < seen[s[l]]:
                        have -= 1
                l += 1
        if not splice:
            return ""
        return s[splice[0]:splice[1]+1]