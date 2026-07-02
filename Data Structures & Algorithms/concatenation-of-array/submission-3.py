class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            num = nums[i]
            result.append(num)
        
        for j in range(len(nums)):
            a = nums[j]
            result.append(a)

        return result