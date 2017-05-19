class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        # time O(1) space (1)
        while n:
            n = n & n-1 # flip least significant 1-bit to 0
            result += 1
        return result