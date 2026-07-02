class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for words in strs:
            key = ''.join(sorted(words))

            if key not in hash_map:
                hash_map[key] = []

            hash_map[key].append(words)
            results = list(hash_map.values())

        return results