class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}

        for i in range(len(nums)):
            num = nums[i]
            comp = target - num

            if comp in dict:
                return [dict[comp], i]

            dict[num] = i

        return [-1, -1]