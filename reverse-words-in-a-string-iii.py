class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # beats 74%
        return " ".join(map(lambda x: x[::-1], s.split()))
        
        # beats 23%
        words = s.split()
        res = ""
        for word in words:
            res = res + word[::-1] + " " 
        res = res.strip()
            
        return res