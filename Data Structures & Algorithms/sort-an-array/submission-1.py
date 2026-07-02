class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        # Base case: if array has 1 or 0 elements, it's already sorted
        if len(nums) <= 1:
            return nums
        
        # Divide
        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])
        
        # Merge
        return self.merge(left, right)
    
    def merge(self, left: list[int], right: list[int]) -> list[int]:
        merged = []
        i = j = 0
        
        # Merge two sorted arrays
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        
        # Add remaining elements
        while i < len(left):
            merged.append(left[i])
            i += 1
        while j < len(right):
            merged.append(right[j])
            j += 1
        
        return merged
