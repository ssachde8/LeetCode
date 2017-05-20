class Solution(object):
    def repeatedSubstringPattern(self, str):
        """
        :type s: str
        :rtype: bool
        """
        if not str or len(str) < 2:
            return False

        strlen = len(str)
        pos = strlen / 2
        while pos > 0:
            if strlen % pos == 0:
                substr = str[:pos]
                divisor = strlen / pos
                if substr*divisor == str:
                    return True
            pos -= 1
        return False
        