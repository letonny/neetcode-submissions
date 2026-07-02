class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # s: source string we search
        # t: target string we need

        # if t is empty theres nothing we need
        if t == "":     
            return ""

        countT = {}     # frequency map for t
        window = {}     # frequency for current window for s

        # begins counting for char in t
        for c in t:
            countT[c] = countT.get(c, 0) + 1 

        # unique char for current window to meet requirement
        have = 0
        # unique char in t
        need = len(countT) 

        # for start + end of current best window
        res = [-1, -1] 

        # length of current best window
        resLen = float("infinity") 

        # left pointer of sliding window
        l = 0 

        # expand window to right
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            # if c is in countT & meets requirement
            if c in countT and window[c] == countT[c]:
                have += 1

            # current window is valid - shrink to find minimum window
            while have == need:
                # update shortest window, if smaller update res/resLen
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1
                
                # shrink window from left
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        #extract substring from res
        l = res[0]
        r = res[1]

        if resLen != float('infinity'):
            return s[l:r + 1]
        else:
            return ''