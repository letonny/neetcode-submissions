class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}

        for i in range(len(nums)):
            num = nums[i]

            if num in dic:
                return True
            
            dic[num] = i
            
        return False