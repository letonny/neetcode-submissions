class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d1 = {}

        for i in range(len(nums)):
            num = nums[i]

            comp = target - num

            if comp in d1:
                return [d1[comp], i]
            
            d1[num] = i

        return [-1, -1]