class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in xrange(len(s)):
            res *= 26
            res += ord(s[i]) - ord('A') + 1
        return res