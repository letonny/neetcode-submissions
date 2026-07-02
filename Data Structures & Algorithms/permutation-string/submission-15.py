class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        need = {}
        window = {}

        for c in s1:
            need[c] = need.get(c, 0) + 1

        left = 0
        for right in range(len(s2)):
            c = s2[right]
            window[c] = window.get(c, 0) + 1

            if (right - left + 1) > len(s1):
                leftChar = s2[left]
                window[leftChar] -= 1

                if window[leftChar] == 0:
                    del window[leftChar]
                left += 1

            if window == need:
                return True
        
        return False