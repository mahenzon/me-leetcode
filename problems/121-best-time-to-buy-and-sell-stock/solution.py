class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif (profit := (price - min_price)) > max_profit:
                max_profit = profit

        return max_profit
