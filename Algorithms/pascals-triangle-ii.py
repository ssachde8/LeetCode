class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1] + [0] * rowIndex
        for i in range(1, rowIndex+1):
            for j in range(i, 0, -1):
                res[j] = res[j] + res[j-1]
        return res