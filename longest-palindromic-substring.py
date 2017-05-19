class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # O(n^2) time and O(1) space
        max_len, start, s_len = 1, 0, len(s)
        low, high = 0, 0
        
        # Consider each char or pair of char as center for odd & even palindromes
        for i in range(1, s_len):
            # Find even length palindrome with center points as i-1 & i
            low, high = i-1, i
            while low >= 0 and high < s_len and s[low] == s[high]:
                if high - low + 1 > max_len: # if current centers make larger palin
                    start = low # point low to start of new palindrome
                    max_len = high - low + 1    # update max_len
                low -= 1
                high += 1
                
            # Find odd length palindrome with center point as i
            low, high = i-1, i+1
            while low >= 0 and high < s_len and s[low] == s[high]:
                if high - low + 1 > max_len:
                    start = low
                    max_len = high - low + 1
                low -= 1
                high += 1
        
        return s[ start: start+max_len ]
            
        