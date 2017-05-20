class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # m * n  matrix
        m = len(matrix) # rows
        
        if m == 0:
            return False
            
        n = len(matrix[0]) # cols
        if n == 0:
            return False
            
        count = 0
        i = 0
        j = n - 1
        while i < m and j >= 0:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
        