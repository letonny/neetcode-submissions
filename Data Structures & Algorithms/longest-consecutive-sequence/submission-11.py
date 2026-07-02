class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s1 = set(nums)
        longest = 0

        for num in nums:
            if num - 1 not in s1:
                current = num
                length = 1
            
                while current + 1 in s1:
                    current += 1
                    length += 1
                
                longest = max(longest, length)
            
        return longest