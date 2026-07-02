class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # hashmap

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        # sorted(iterable, key=function, reverse=True)
        #   iterable = dictionary keys
        #   key =  count.get
        #   reverse = sort descending
        #   sorted(....) returns list of keys
        #   [:k] = slice syntax to take first k items from the list
        return sorted(count, key=count.get, reverse=True)[:k]
    