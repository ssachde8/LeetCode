class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = [str(x) for x in digits]
        num = int(''.join(digits)) + 1
        return [int(x) for x in str(num)]