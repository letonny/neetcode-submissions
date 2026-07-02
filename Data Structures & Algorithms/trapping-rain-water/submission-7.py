class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        rightMax = 0
        leftMax = 0
        water = 0

        while left < right:
            if height[left] < height[right]:
                if leftMax <= height[left]:
                    leftMax = height[left]
                else:
                    water += leftMax - height[left]
                left += 1
            else:
                if rightMax <= height[right]:
                    rightMax = height[right]
                else:
                    water += rightMax - height[right]
                right -= 1
        
        return water