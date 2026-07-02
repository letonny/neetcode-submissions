class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            number = nums[i]

            find_num = target - number

            if find_num in seen:
                return [seen[find_num], i]

            seen[number] = i
        
        return [-1, -1]