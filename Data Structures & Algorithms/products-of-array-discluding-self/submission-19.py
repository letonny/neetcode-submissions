class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [0] * len(nums)
        post = [0] * len(nums)
        res = [0] * len(nums)

        bef = 1
        for i in range(len(nums)):
            pre[i] = bef
            bef *= nums[i]

        aft = 1
        for i in range(len(nums) - 1, -1, -1):
            post[i] = aft
            res[i] = pre[i] * post[i]
            aft *= nums[i]
        
        return res