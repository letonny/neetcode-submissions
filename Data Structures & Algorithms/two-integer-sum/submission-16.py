class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dupe = {}

        for i in range(len(nums)):
            num = nums[i]
            comp = target - num

            if comp in dupe:
                return [dupe[comp], i]
            
            dupe[num] = i
        
        return [-1, -1]