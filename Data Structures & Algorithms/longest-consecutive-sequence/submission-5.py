class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s1 = set(nums)  # get rids of dupes
        longest = 0 # used later to find max sequence

        for num in nums:
            if num - 1 not in s1:
                cur = num
                length = 1

                while cur + 1 in s1:
                    cur += 1
                    length += 1
                
                longest = max(longest, length)
        
        return longest

