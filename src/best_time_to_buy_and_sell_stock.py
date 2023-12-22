# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
import sys


class Solution:

    # This is the first solution that I came up with. Almost half of the test cases failed.
    # O(n) with two passes.
    @staticmethod
    def best_time_to_buy_and_sell_stock_iteration_0(prices: list[int]) -> int:
        if len(prices) == 0:
            return 0

        minimum = sys.maxsize
        minimum_index = 0

        # Find out the best day to purchase.
        for i in range(len(prices)):
            # Check for min. value first.
            if prices[i] < minimum:
                minimum = prices[i]
                minimum_index = i

        if minimum_index == len(prices) - 1:
            return 0

        # Construct a new array to choose sell day.
        sell_days = [0] * len(prices)
        itr = 0
        maximum = -1
        for j in range(minimum_index + 1, len(prices)):
            sell_days[itr] = prices[j]
            itr += 1

            if prices[j] > maximum:
                maximum = prices[j]

        return maximum - minimum

    # Using of built-in 'max' for calculation.
    @staticmethod
    def best_time_to_buy_and_sell_stock_iteration_1(prices: list[int]) -> int:
        profit = 0
        buy = prices[0]

        for sell in prices[1:]:
            if sell > buy:
                profit = max(profit, sell - buy)
            else:
                buy = sell

        return profit
