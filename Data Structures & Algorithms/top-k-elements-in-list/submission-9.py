class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        k_map = {}
        for num in nums:
            if num not in k_map:
                k_map[num] = 1
            else:
                k_map[num] += 1

        bucket = [[] for i in range(len(nums) + 1)]
        for count, key in k_map.items():
            bucket[key].append(count)
        
        ans = []
        for i in range(len(bucket) -1, 0, -1):
            for j in bucket[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans