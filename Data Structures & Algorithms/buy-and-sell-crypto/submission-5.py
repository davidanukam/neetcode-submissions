class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for i, num in enumerate(prices):
            profit = max(profit, num - buy)
            buy = min(buy, num)
        return profit