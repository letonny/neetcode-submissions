class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        s1 = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in s1:
                s1[key] = [word]
            else:
                s1[key].append(word)
            
        return list(s1.values())