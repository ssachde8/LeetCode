class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        # refer : http://www.geeksforgeeks.org/print-palindromic-partitions-string/
        # backtraccking method
        result = []
        self.backtrack(s, [], result)
        return result
        
        
    def backtrack(self, s, path, res):
        if not s: # backtracking, add partitions to result
            res.append(path[:]) # : ensures that we just append current elements
        for i in range(1, len(s)+1):
            if self.isPali( s[ :i ] ):
                path.append( s[:i] ) # hold current partitions
                self.backtrack( s[ i: ], path, res) # check for new partitions
                # change the current partition vector to the old 
                # one as it might have changed in the recursive step.
                path.pop()
        
    def isPali(self, s):
        for i in xrange(len(s) / 2):
            if s[i] != s[-(i + 1)]:
                return False
        return True
        
        
        