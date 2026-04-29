class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i, num1 in enumerate(prices):
            for j, num2 in enumerate(prices):
                if j > i:
                    diff = num2 - num1
                    if diff > profit:
                        profit = diff
        return profit