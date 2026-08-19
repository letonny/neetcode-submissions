import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Build frequency map
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        # Step 2: Use a min-heap to keep track of the top k elements.
        # We store (frequency, number) tuples.
        min_heap = []
        for num, freq in count.items():
            heapq.heappush(min_heap, (freq, num))
            
            # If the heap size exceeds k, remove the smallest frequency element.
            if len(min_heap) > k:
                heapq.heappop(min_heap)
            
        # Step 3: Extract just the numbers from the heap tuples.
        return [num for freq, num in min_heap]