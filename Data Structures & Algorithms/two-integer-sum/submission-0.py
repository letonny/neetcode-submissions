class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}

        for i in range(len(nums)):
            num = nums[i]

            comp = target - num

            if comp in dic:
                return [dic[comp], i]

            dic[num] = i

        return [-1, -1]
        