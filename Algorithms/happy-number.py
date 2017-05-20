class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        lookup = {}
        while n != 1 and n not in lookup:
            lookup[n] = True
            n = self.nextNumber(n)
        return n == 1
        
        
    def nextNumber(self, n):
        new = 0
        for digit in str(n):
            new += int(digit)**2
        return new