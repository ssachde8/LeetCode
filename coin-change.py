class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        INF = 0x7fffffff  # Using float("inf") would be slower.
        table = [INF] * (amount + 1)
        table[0] = 0
        for i in xrange(amount + 1):
            if table[i] != INF:
                for coin in coins:
                    if i + coin <= amount:
                        table[i + coin] = min(table[i + coin], table[i] + 1)
        return table[amount] if table[amount] != INF else -1