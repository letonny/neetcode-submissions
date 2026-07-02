class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        seen = [False] * n

        for num in nums:
            if num > 0 and num <= n:
                seen[num - 1] = True
        
        for num in range(1, n + 1):
            if not seen[num - 1]:
                return num
        
        return n + 1


    #   [   1      2      4   ] : n = 3
    #   [ False  False  False ] 
    #   [ True   False  False ] : 1
    #   [ True   True   False ] : 2
    #   [ True   True   False ] : 4
    #   [   0      1      2   ]

    #   range(1, 4)
    #   seen[1 - 1] -> seen[0] = True
    #   seen[2 - 1] -> seen[1] = True
    #   seen[3 - 1] -> seen[2] = False
    #   returns num