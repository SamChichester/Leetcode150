"""

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day
in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = float('inf')
        max_price = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > max_price:
                max_price = price - min_price

        return max_price


if __name__ == "__main__":
    solution = Solution()
    prices1 = [7, 1, 5, 3, 6, 4]
    max_profit1 = solution.maxProfit(prices1)
    assert max_profit1 == 5
    prices2 = [7, 6, 4, 3, 1]
    max_profit2 = solution.maxProfit(prices2)
    assert max_profit2 == 0
