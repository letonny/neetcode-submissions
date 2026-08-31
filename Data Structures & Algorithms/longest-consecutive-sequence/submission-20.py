class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        s1 = set(nums)

        for num in s1:
            if num - 1 not in s1:
                length = 1

                while length + num in s1:
                    length += 1
                
                max_len = max(max_len, length)
        
        return max_len