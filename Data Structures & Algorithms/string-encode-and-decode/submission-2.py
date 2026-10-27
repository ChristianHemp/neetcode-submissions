class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strings = []

        for string in strs:
            encoded_strings.append(f"{len(string)}%{string}")

        return ''.join(encoded_strings)

    def decode(self, s: str) -> List[str]:
        decoded_strings = []
        i = 0
        j = 0
        while i < len(s):
            while s[j] != '%':
                j += 1
            next_string_length = int(s[i:j])
            decoded_strings.append(s[j + 1: j + next_string_length + 1])
            
            j += next_string_length + 1
            i = j

        return decoded_strings