class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        for i in xrange(len(prices)-1):
            price = prices[i+1] - prices[i]
            profit += max(0, price)
        return profit