class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d1 = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key not in d1:
                d1[key] = []

            d1[key].append(word)

        return list(d1.values())