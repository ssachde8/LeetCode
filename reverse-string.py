class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # beats 96%
        return s[::-1]
        
        # beats 24% solutions
        s = list(s)
        i, j = 0, len(s)-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -=1
        return "".join(s)