class Solution:
    def groupAnagrams(self, strs):
        anagram_map = {}  # key: sorted string, value: list of strings
        
        for s in strs:
            key = ''.join(sorted(s))  # sort the string to create the key
            if key not in anagram_map:
                anagram_map[key] = []
            anagram_map[key].append(s)
        
        return list(anagram_map.values())
