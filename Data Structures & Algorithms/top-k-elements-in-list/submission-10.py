class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f_map = {}  #   CREATE MAPPING FOR {NUM, COUNT}
    
        for num in nums:    
            if num not in f_map:
                f_map[num] = 1 #    IF NUM HAVE NOT BEEN FOUND PUT 1
            else:
                f_map[num] += 1 #   IF NUM ALREADY EXISTED ADD 1 TO THE COUNT

        # COUNT = BUCKET INDEX
        bucket = [[] for i in range(len(nums) + 1)] #   + 1 THE LENGTH BECAUSE SIZE = COUNT
        for num, count in f_map.items(): #  LOOPS THROUGH THE DICTIONARY
            bucket[count].append(num)   #   ADDS NUM TO CORRESPONDING COUNT OF THE BUCKET INDEX
        
        ans = [] #  CREATE A NEW ARRAY TO RETURN
        for i in range(len(bucket) -1, 0 , -1): #   OUTER LOOP: REVERSES HIGH COUNT -> LOW COUNT
            for num in bucket[i]: #     INNER LOOP TO ADD NUM TO NEW ARR
                ans.append(num)
            if len(ans) == k: #     STOPS ADDING ONCE SIZE 'K' OF ARRAY IS REACHED
                return ans