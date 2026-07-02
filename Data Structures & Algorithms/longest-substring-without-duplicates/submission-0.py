class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()       # track characters in the current window
        max_length = 0     # store the length of the longest substring
        start = 0          # left pointer of the window

        for end in range(len(s)):
            # if s[end] is already in the window, remove characters from the start
            while s[end] in seen:
                seen.remove(s[start])
                start += 1
            
            # add current character to the window
            seen.add(s[end])
            
            # update maximum length
            max_length = max(max_length, end - start + 1)
        
        return max_length
