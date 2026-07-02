class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # insert 0s into array same size as list
        output = [0] * n

        pre = 1

        for i in range(n):
            output[i] = pre
            pre *= nums[i]
        
        post = 1

        for i in range(n - 1, - 1, -1):
            output[i] *= post
            post *= nums[i]
        
        return output

