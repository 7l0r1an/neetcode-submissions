class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_max = 0
        profit = -1
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                if profit > profit_max:
                    profit_max = profit
        return profit_max
