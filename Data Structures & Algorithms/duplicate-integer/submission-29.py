class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s1 = set()

        for n in nums:
            if n in s1:
                return True
            s1.add(n)

        return False
				   