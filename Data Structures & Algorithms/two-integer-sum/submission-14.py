class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h1 = {}

        for i in range(len(nums)):
            num = nums[i]
            comp = target - num

            if comp in h1:
                return [h1[comp], i]
            
            h1[num] = i
        
        return [-1, -1]