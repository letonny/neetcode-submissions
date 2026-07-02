class Solution:
    def encode(self, strs):
        # Encode list of strings to a single string
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s):
        # Decode single string back to list of strings
        res, i = [], 0
        while i < len(s):
            # Find the separator #
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            # Extract the string
            res.append(s[j+1:j+1+length])
            # Move i to the next encoded string
            i = j + 1 + length
        return res
