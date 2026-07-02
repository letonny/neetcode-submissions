class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = {}  # TRACKS FREQ OF EACH CHAR
        res = 0     # MAX WINDOW LENGTH
        left = 0    # LEFT SIDE OF WINDOW
        maxFreq = 0 # COUNT OF MOST COMMON CHARACTER


        for right in range(len(s)):                     # EXPANDS THE WINDOW
            count[s[right]] = count.get(s[right], 0) + 1   # ADD CUR CHAR TO FREQ MAP
            maxFreq = max(maxFreq, count[s[right]])     # KEEPS TRACK OF HIGHEST FREQ CHARACTER

            while (right - left + 1) - maxFreq > k:     # CHECK IF WINDOW INVALID ( WINDOW SIZE MINUS MAX FREQ )
                count[s[left]] -= 1                     # SHRINKS THE WINDOW - REMOVING LEFTMOST CHAR
                left += 1                               # MOVE LEFT POINTER FORWARD
            
            res = max(res, right - left + 1)            # KEEP TRACK OF LARGEST WINDOW SEEN

        return res