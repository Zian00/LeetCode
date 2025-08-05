class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        low = prices[0]
        high = prices[0]
        profit = 0
        n = len(prices)

        while i < n-1:
            # find low (buy point)
            while i < n-1 and prices[i] >= prices[i + 1]:
                i += 1
                low = prices[i]

            # find high (sell point)
            while i < n-1 and prices[i] <= prices[i + 1]:
                i += 1
            high = prices[i]
            profit += high - low
        return profit



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit =0
        for i in range(len(prices)-1):
            if prices[i+1] - prices[i] > 0:
                profit += prices[i+1] - prices[i]
        return profit