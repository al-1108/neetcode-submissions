class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded_string = ""
        for string in strs:
            encoded_string += (str(len(string)) + "#" + string)
        return encoded_string
    def decode(self, s: str) -> list[str]:
        decoded_string = []
        index = 0
        while index < len(s):
            string = ""
            number_of_chars = ""
            while s[index] != "#":
                number_of_chars += s[index]
                index += 1
            index += 1
            for _ in range(int(number_of_chars)):
                string += s[index]
                index += 1
            decoded_string.append(string)
        return decoded_string