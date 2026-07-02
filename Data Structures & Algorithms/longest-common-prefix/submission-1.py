class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == "":
            return ""

        prefix = ""
        shortest = min(strs, key = len)

        for i in range(len(shortest)):
            char = shortest[i]

            if all(s[i] == char for s in strs):
                prefix += char
            else:
                break
            
        return prefix