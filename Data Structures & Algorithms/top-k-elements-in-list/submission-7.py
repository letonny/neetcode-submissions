class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_map = {} # CREATE MAPPING FOR {NUM, COUNT}
    
        for num in nums:
            if num not in f_map:
                f_map[num] = 1
            else:
                f_map[num] += 1

        # COUNT = BUCKET INDEX
        bucket = [[] for i in range(len(nums) + 1)] 
        for num, count in f_map.items():
            bucket[count].append(num)
        
        ans = []
        for i in range(len(bucket) -1, 0 , -1):
            for num in bucket[i]:
                ans.append(num)
            if len(ans) == k:
                return ans