class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        while len(prices) > 0:
            mi = min(prices)
            mx = max(prices[prices.index(mi):])
            profits.append(mx - mi)
            prices.remove(mi)
        return max(profits) if len(profits) > 0 else 0