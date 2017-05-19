class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d1, d2 =[0] * 26, [0]*26
        for char in s:
            d1[ord(char)-ord('a')] += 1
        for char in t:
            d2[ord(char)-ord('a')] += 1
        return d1 == d2