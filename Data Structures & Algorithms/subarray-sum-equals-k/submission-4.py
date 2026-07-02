class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0                  # To keep track of the number of subarrays
        current_sum = 0            # Running sum of elements
        prefix_sums = {0: 1}       # Initialize hashmap with 0 sum seen once

        for num in nums:
            current_sum += num
            # Check if there is a previous prefix sum that would make a subarray sum = k
            if current_sum - k in prefix_sums:
                count += prefix_sums[current_sum - k]
            # Update the prefix_sums map
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1

        return count
