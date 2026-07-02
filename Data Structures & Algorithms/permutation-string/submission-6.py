class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        c1 = {}

        for c in s1:
            c1[c] = c1.get(c, 0) + 1
        
        need = len(c1)

        for i in range(len(s2)):
            c2 = {}
            cur = 0

            for j in range(i, len(s2)):
                c2[s2[j]] = c2.get(s2[j], 0) + 1

                if c1.get(s2[j], 0) < c2[s2[j]]:
                    break
                
                if c1.get(s2[j], 0) == c2[s2[j]]:
                    cur += 1
                
                if need == cur:
                    return True
        
        return False