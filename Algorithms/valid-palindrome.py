class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s)-1
        s = s.lower()
        
        while left<right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            elif s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True