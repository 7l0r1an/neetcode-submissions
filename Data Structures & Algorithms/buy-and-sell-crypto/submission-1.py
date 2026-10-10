class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit_max = 0
        profit = -1
        min_price = 100000
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            profit = prices[i] - min_price
            if profit > profit_max:
                profit_max = profit
        return profit_max
