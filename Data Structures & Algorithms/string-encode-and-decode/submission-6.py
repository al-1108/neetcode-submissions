class Solution:
    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += str(len(s)) + "#" + s
        return string
    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        while i < len(s):
            string = ""
            string_chars = ""
            while s[i] != "#":
                string_chars += s[i]
                i += 1
            i += 1
            for _ in range(int(string_chars)):
                string += s[i]
                i += 1
            strs.append(string)
        return strs


            

