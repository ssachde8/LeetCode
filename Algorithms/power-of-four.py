class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num and not (num & 0b11):
            num >>= 2
        return (num == 1)