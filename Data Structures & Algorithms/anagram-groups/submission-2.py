class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagrams = {}

        for string in strs:
            sorted_str = ''.join(sorted(string))

            if sorted_str not in anagrams:
                anagrams[sorted_str] = [string]
            else:
                anagrams[sorted_str].append(string)
        
        return list(anagrams.values())
            