class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currSum = count = 0
        prefixSum = {0 : 1}

        for num in nums:
            currSum += num
            diff = currSum - k

            count += prefixSum.get(diff, 0)
            prefixSum[currSum] = 1 + prefixSum.get(currSum, 0)
        
        return count