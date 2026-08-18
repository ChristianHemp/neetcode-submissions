class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {}

        for char in s:
            if char in hash_map:
                hash_map[char] += 1
            else:
                hash_map[char] = 1
        
        for char in t:
            if char not in hash_map:
                return False
            else:
                hash_map[char] -= 1
                if(hash_map[char] < 0):
                    return False
        
        if max(hash_map.values()) > 0:
            return False

        return True
