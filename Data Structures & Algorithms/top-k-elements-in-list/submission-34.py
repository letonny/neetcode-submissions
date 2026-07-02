class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # create a hash map:
        count = {}

        # build a frequency map:
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # build a heap

        heap = []

        # create tuple in heap map using (frequency, number) from freq map

        for num in count:
            heapq.heappush(heap,(count[num], num))
        
            # if the tuple list exceeds k -> reduce it
            if len(heap) > k:
                heapq.heappop(heap)
            
        # create an array to print the results

        ans = []

        for i in range(k):
            # index 1 is picks the num instead of freq
            ans.append(heapq.heappop(heap)[1]) 
        
        return ans