class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n - 1

        while left < right:
            num = numbers[left] + numbers[right]

            if num == target:
                return [left + 1, right + 1] # 1 - indexed list
            elif num < target:
                left += 1
            else:
                right -= 1
        
