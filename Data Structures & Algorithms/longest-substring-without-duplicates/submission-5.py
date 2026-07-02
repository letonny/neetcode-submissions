class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        result = 0

        for i in range(n):
            seen = set()

            for j in range(i, n):
                if s[j] in seen:
                    break
                seen.add(s[j])
                result = max(result, len(seen))


        return result