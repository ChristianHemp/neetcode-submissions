from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = defaultdict(list)

        for s in strs:
            counts = [0] * 26

            for c in s:
                counts[ord(c) - ord('a')] += 1
            
            hm[tuple(counts)].append(s)
        
        return list(hm.values())