class Solution(object):
    def rotate(self, A):
        """
        First, reverse up to down.
        Second, swap symmetrically. eg. 0,2 with 2,0
        """
        A.reverse()
        for i in range(len(A)):
            for j in range(i):
                # swap
                A[i][j], A[j][i] = A[j][i], A[i][j]
        