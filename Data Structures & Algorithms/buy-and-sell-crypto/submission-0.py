class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_seen = float('inf')

        for i in range(len(prices)):
            if prices[i] < min_seen:
                min_seen = prices[i]
            else:
                max_profit = max(max_profit, prices[i] - min_seen)
        
        return max_profit