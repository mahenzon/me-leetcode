class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        state: Buying or Selling?

        If buy -> i + 1
        if sell -> i + 2 (add cooldown day)

        """
        prices_len = len(prices)
        # key = (i, buying)
        # value = max_profit
        cache: dict[tuple[int, bool], int] = {}

        def depth_first_search(i: int, buying: bool):
            if i >= prices_len:
                return 0
            if (i, buying) in cache:
                return cache[(i, buying)]

            next_day = i + 1
            current_price = prices[i]
            cooldown = depth_first_search(next_day, buying)
            if buying:
                buy = depth_first_search(next_day, not buying) - current_price
                cache[(i, buying)] = max(buy, cooldown)
            else:
                # sell adds one cooldown day!
                sell = depth_first_search(next_day + 1, True) + current_price
                cache[(i, buying)] = max(sell, cooldown)

            return cache[(i, buying)]

        return depth_first_search(0, True)
