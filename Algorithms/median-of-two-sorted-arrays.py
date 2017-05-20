class Solution(object):
    
    
        
    
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        def median(a):
            if len(a) % 2 != 0:
                return a[len(a)//2]
            else:
                return ( (a[len(a)/2] + a[(len(a)/2)-1]) / 2.0)
                
        temp = nums1+nums2
        temp.sort()
        return (median(temp))