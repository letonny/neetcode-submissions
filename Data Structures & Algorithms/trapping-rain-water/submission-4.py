class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        mLeft = 0
        mRight = 0

        result = 0 

        while left < right:
            if height[left] < height[right]:
                if height[left] >= mLeft:
                    mLeft = height[left]
                else:
                    result += mLeft - height[left]
                left += 1

            else:
                if height[right] >= mRight:
                    mRight = height[right]
                else:
                    result += mRight - height[right]
                right -= 1
        
        return result