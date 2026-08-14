class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s1 = set(nums)

        return len(nums) != len(s1)