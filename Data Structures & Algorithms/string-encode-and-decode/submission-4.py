class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strings = []

        for string in strs:
            encoded_strings.append(f"{len(string)}%{string}")
        
        return ''.join(encoded_strings)


    def decode(self, s: str) -> List[str]:
        result = []
        index = 0
        forward_ptr = 0

        while index < len(s):
            while s[forward_ptr] != '%':
                forward_ptr += 1

            curr_length = int(s[index:forward_ptr])
            result.append(s[forward_ptr + 1: forward_ptr + curr_length + 1])

            forward_ptr += curr_length + 1
            index = forward_ptr
        
        return result