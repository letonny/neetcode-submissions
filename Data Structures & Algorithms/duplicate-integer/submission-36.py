class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s1 = set()

        for c in nums:
            if c in s1:
                return True
            s1.add(c)
        
        return False