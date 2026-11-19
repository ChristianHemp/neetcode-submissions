from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        result = []

        for string in strs:
            char_counts = [0] * 26

            for char in string:
                char_counts[ord(char) - ord('a')] += 1
            
            groups[tuple(char_counts)].append(string)
        
        for sublist in groups.values():
            result.append(sublist)
        
        return result