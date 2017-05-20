class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        odds = 0
        cnt_s = collections.Counter(s)
        for _, val in cnt_s.items():
            odds = odds + ( val & 1)
            
        return len(s) - odds + int(odds > 0)
            