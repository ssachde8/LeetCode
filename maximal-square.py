class Solution(object):
    def maximalSquare(self, a):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not a: 
            return 0
        m, n, result = len(a), len(a[0]), 0
        b = [ [0 for _ in range(n+1)] for i in range(m+1) ]
        # b[i][j] represent the edge length of the largest square ENDING at position (i, j)
        for i in range(1, m+1):
            for j in range(1, n+1):
                if a[i-1][j-1] == '1':
                    b[i][j] = min( min(b[i][j-1], b[i-1][j-1]) , b[i-1][j]) + 1
                    result = max(b[i][j], result)
        
        return result *result
        