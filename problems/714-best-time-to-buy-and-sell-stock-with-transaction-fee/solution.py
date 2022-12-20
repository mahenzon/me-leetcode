class Solution:
    def maxProfit(self, prices: list[int], fee: int) -> int:
        profit = 0
        state = -prices[0]
        for idx in range(1, len(prices)):
            price = prices[idx]
            profit = max(profit, state + price - fee)
            state = max(state, profit - price)

        return profit
