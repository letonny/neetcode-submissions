class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        gram = {}

        for word in strs:
            key = ''.join(sorted(word))

            if key in gram:
                gram[key].append(word)
            else:
                gram[key] = [word]
            
        return list(gram.values())