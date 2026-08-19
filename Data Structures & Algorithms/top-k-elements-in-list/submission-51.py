class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        m_heap = []

        for num, freq in count.items():
            heapq.heappush(m_heap, (freq, num))

            if len(m_heap) > k:
                heapq.heappop(m_heap)
        
        return [num for freq, num in m_heap]