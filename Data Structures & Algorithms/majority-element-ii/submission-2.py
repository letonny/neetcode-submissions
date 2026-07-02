class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        k_map = {}
        ans = []
        n = len(nums)

        for num in nums:
            if num not in k_map:
                k_map[num] = 1
            else:
                k_map[num] += 1

        for keys, values in k_map.items():
            if values > n // 3:
                ans.append(keys)
        
        return ans