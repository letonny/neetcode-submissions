class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {}

        for i in range(len(nums)):
            num = nums[i]
            comp = target - num

            if comp in h_map:
                return [h_map[comp], i]

            h_map[num] = i

        return [-1, -1]