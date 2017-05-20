class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        letter_pos = {} # track number of unique characters
        sub_start = 0 # new substring index
        max_len = 0 # final ans
        
        for i in range(len(s)):
            if ( s[i] in letter_pos )  and  ( sub_start <= letter_pos[s[i]] ): # new possible substring
                sub_start = letter_pos[s[i]] + 1
            else:
                max_len = max(max_len, i - sub_start + 1) # max(_, window_size)
            letter_pos[s[i]] = i
            
        return max_len