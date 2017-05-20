from collections import defaultdict

class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        if s is None or len(s) == 0 or p is None or len(p) == 0:
            return res
        lookup = defaultdict(int)
        # record each character in p to hash
        for char in p:
            lookup[char] += 1
            
        left, right, count = 0, 0, len(p)
        while right < len(s):
            if lookup[s[right]] >= 1:
                count -= 1
                lookup[s[right]] -= 1
                right += 1
                
                
            if count == 0:
                res += str(left);
                
            if right-left == len(p) and lookup[s[left]] >= 0:
                count += 1
                lookup[s[left]] += 1
                left += 1
        
        return res