class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxLeft = 0
        maxRight = 0 
        water = 0

        while left < right:
            if height[left] < height[right]:
                if maxLeft <= height[left]:
                    maxLeft = height[left]
                else:
                    water += maxLeft - height[left]
                left += 1
            else:
                if maxRight <= height[right]:
                    maxRight = height[right]
                else:
                    water += maxRight - height[right]
                right -= 1
        
        return water