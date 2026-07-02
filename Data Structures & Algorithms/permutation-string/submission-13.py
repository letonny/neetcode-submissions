class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        need = {}
        count = {}

        for c in s1:
            need[c] = need.get(c, 0) + 1

        left = 0
        for right in range(len(s2)):
            c = s2[right]
            count[c] = count.get(c, 0) + 1

            if (right - left + 1) > len(s1):
                leftChar = s2[left]
                count[leftChar] -= 1

                if count[leftChar] == 0:
                    del count[leftChar]
                left += 1

            if count == need:
                return True
        
        return False