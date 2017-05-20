class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = 0
        for i in range(32):
            result <<= 1 # left shift by 1
            # n&1 returns last digit, bitwise or is chepear than add
            result = result | (n & 1)
            n >>= 1 # right shift by 1, update n
        return result