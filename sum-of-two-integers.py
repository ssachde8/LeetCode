class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 bits integer max and min
        MAX = 0x7FFFFFFF
        MIN = 0x80000000
        MASK = 0xFFFFFFFF   # mask to extract last 32 bits
        
        while b != 0:
             # ^ get different bits and & gets double 1s, << moves carry
            c = (a & b) & MASK
            a = (a ^ b) & MASK
            b = (c << 1) & MASK
        
        if a <= MAX:
            return a
        else:
            return ~(a ^ MASK)