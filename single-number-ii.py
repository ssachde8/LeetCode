class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum1 = sum(set(nums)) * 3 # multiply sum of unique numbers by frequency 
        sum2 = sum(nums)    # normal sum including repeated entries
        ans = (sum1 - sum2)/2   # return element occuring once
    
        return ans
