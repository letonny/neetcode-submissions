class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}

        for letter in s1:
            count1[letter] = count1.get(letter, 0) + 1
        
        need = len(count1)

        for letter in range(len(s2)):
            count2 = {}
            current = 0

            for j in range(letter, len(s2)):
                count2[s2[j]] = count2.get(s2[j], 0) + 1

                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break
                
                if count1.get(s2[j], 0) == count2[s2[j]]:
                    current += 1
                
                if current == need:
                    return True
        
        return False