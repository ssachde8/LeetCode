class Solution(object):
    def wordBreak(self, s, words):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        possible = [False for _ in range(len(s)+1)] # dp table for sub-problems
        
        possible[0] = True  # mark first sub-problem True
        
        for i in range(1, len(s)+1):    # 1 -> len(s) + 1
            for j in range(i):  # find sub_strings
                sub = s[j:i]
                if possible[j] and sub in words:    # if both halves in dp
                    possible[i] = True # True if there is a word in the dictionary that ends at ith index of s
                    break
            
        return possible[len(s)]
        