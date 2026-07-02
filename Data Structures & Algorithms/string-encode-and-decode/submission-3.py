class Solution:
    def encode(self, strs):
        # Encode list of strings into one string
        res = ""
        for s in strs:
            # Store length + a delimiter + the string itself
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s):
        # Decode single string back to list of strings
        res = []
        i = 0
        while i < len(s):
            # Find the delimiter (#)
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])  # length of string
            word = s[j+1:j+1+length]  # extract substring
            res.append(word)
            i = j + 1 + length  # move to next encoded word
        return res
