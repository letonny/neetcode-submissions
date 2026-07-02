from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        min_price = prices[0]   # lowest price so far
        max_profit = 0          # maximum profit so far
        
        for price in prices:
            # calculate potential profit if selling today
            profit = price - min_price
            max_profit = max(max_profit, profit)
            
            # update min_price if current price is lower
            min_price = min(min_price, price)
        
        return max_profit
