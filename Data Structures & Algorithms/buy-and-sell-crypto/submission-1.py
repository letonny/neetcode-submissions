class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        min_price = prices[0]   # lowest price so far
        max_profit = 0          # maximum profit so far
        
        for price in prices:
            # calculate potential profit if selling today
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
            
            # update min_price if current price is lower
            if price < min_price:
                min_price = price
        
        return max_profit
