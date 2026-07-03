class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s1 = {}

        for num in nums:
            s1[num] = s1.get(num, 0) + 1

        heap = []

        for num in s1:
            heapq.heappush(heap, (s1[num], num))
        
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []

        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res