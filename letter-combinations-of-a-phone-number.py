class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        # Iterative Solution
        if not digits:
            return []
            
        lookup = ["", "", "abc", "def", "ghi", "jkl", "mno", \
                          "pqrs", "tuv", "wxyz"]
        result = [""]
                          
        for digit in reversed(digits):
            choices = lookup[int(digit)] # for eg. "abc"
            
            m, n = len(choices), len(result) # for eg. 3, 1
            
            for i in xrange(n, m * n): # 1 -> 3
                result.append(result[i % n]) # 1%1->0 , 2%1->1, 3%1->2
            
            for i in xrange(m * n):
                result[i] = choices[i / n] + result[i] # 0/3, 1/3, 2/3
                
        return result
                
        