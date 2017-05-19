class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m = 1 # multiplier
        n = len(nums)
        res = []
        for i in range(n):
            res.append(m)
            m = m * nums[i]
        
        m = 1
        for i in range(n-1, -1, -1): # reverse
            res[i] = res[i] * m
            m = m * nums[i]
            
        return res