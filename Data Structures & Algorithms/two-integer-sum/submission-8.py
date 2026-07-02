class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            num = nums[i]

            comp = target - num

            if comp in seen:
                return [seen[comp], i]
            
            seen[num] = i
        
        return [-1, -1]