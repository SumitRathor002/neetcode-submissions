class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if len(prices) < 2:
            return max_profit
        
        i = 0
        j = 1
        while j < len(prices):
            max_profit = max(max_profit, prices[j] - prices[i])
            if prices[j] < prices[i]:
                i = j
            
            j += 1
            
        return max_profit
