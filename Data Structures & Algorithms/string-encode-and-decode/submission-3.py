class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += str(len(string)) + "#" + string
        return encoded_string
    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        index = 0
        while index < len(s):
            string_chars = ""
            string = ""
            while s[index] != "#":
                string_chars += s[index]
                index += 1
            index += 1
            for _ in range(int(string_chars)):
                string += s[index]
                index += 1 
            decoded_strs.append(string)
        return decoded_strs
        

