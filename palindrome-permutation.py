class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s:
            d = []
            l = len(s)
            for i in range(l):
                d.append(s[i]) if s[i] not in d else d.remove(s[i])
            return True if len(d) in (0,1) else False
            