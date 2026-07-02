class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}

        # will build a frequency map
        for letter in s1:
            count1[letter] = count1.get(letter, 0) + 1 
        
        # length for unique letters for s1
        need = len(count1)

        # start to build substring from each letter in s2
        for letter in range(len(s2)):
            
            # resets each time at new letter when building substring
            count2 = {}
            current = 0

            # for expanding the substring forward
            for j in range(letter, len(s2)):
                # count letters in the substring
                count2[s2[j]] = count2.get(s2[j], 0) + 1

                # checks if s1 has letter that s2 has
                if count1.get(s2[j], 0) < count2[s2[j]]:
                    break
                # letter found now find next letter than s2 has
                if count1.get(s2[j], 0) == count2[s2[j]]:
                    current += 1
                # its a match
                if current == need:
                    return True
        
        return False