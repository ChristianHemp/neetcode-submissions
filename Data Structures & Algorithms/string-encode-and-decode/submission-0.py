class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_strs = []

        for s in strs:
            encoded_strs.append(f"{len(s)}%{s}")
        
        return ''.join(encoded_strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        j = 0
        while i < len(s):
            while s[j] != '%':
                j += 1
            
            length = int(s[i:j])
            chars = []

            for _ in range(length):
                j += 1
                chars.append(s[j])
            
            res.append(''.join(chars))
            j += 1
            i = j
        
        return res
