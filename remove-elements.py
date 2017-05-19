class Solution(object):
    def removeElement(self, A, elem):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i, last = 0, len(A) - 1
        while i <= last:
            if A[i] == elem:
                A[i], A[last] = A[last], A[i]
                last -= 1
            else:
                i += 1
        return last + 1