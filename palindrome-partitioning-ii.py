class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # acceleration
        if s == s[::-1]: return 0
        lookup = [[False for k in range(len(s))] for i in range(len(s)) ]
        mincut = [len(s)-1-i for i in range(len(s)+1)]
        
        for i in reversed(xrange(len(s))):
            for j in xrange(i, len(s)):
                if s[i] == s[j]:
                    if j - i < 2 or lookup[i+1][j-1]:
                        lookup[i][j] = True
                        mincut[i] = min(mincut[i], mincut[j+1] + 1)
        return mincut[0]