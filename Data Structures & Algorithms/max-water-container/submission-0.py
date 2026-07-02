from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            # Width between bars
            width = right - left

            # Height is limited by the shorter bar
            current_height = min(height[left], height[right])

            # Calculate area
            area = width * current_height
            max_water = max(max_water, area)

            # Move the pointer with the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
