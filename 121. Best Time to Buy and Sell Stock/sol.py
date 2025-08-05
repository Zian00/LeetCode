class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0]
        profit = 0
        for index, price in enumerate(prices):
            if price < min_price:
                min_price = price
            if price > min_price and (price - min_price) > profit:
                profit = price - min_price
        return profit
