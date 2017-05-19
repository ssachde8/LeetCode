class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        return str(x) == str(x)[::-1]
        
        
        '''
        copy, reverse =  x, 0
        while copy:
            reverse *= 10
            reverse = reverse + copy % 10
            copy /= 10
            
        return x == reverse 
        '''