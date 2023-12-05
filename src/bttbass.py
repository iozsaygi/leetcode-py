# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
import sys


class Solution:

    # This is the first solution that I came up with. Almost half of the test cases failed.
    # O(n) with two passes.
    @staticmethod
    def bttbass_iteration_0(prices: list[int]) -> int:
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
