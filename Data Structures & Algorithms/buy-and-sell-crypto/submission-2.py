class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = prices[0]
        profit = 0
        for price in prices:
            if price < l:
                l = price
            profit = max(profit, price-l)
        return profit
            
        
        
        

        