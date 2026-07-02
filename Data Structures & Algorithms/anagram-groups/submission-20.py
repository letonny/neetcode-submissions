class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key not in ana:
                ana[key] = []
            
            ana[key].append(word)

        return list(ana.values())
        