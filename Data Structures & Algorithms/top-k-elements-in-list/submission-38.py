class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        hmap = []

        for num in count:
            heapq.heappush(hmap, (count[num], num))

            if len(hmap) > k:
                heapq.heappop(hmap)
        
        ans = []

        for i in range(k):
            ans.append(heapq.heappop(hmap)[1])
        
        return ans
        
