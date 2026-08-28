class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s1 = set(nums)
        max_len = 0

        for num in s1: 
            if num - 1 not in s1:
                length = 1

                while (num + length) in s1:
                    length += 1
                
                max_len = max(max_len, length)
            
        return max_len