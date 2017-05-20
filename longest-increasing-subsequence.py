class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        LIS = [] # LIS[i]: the length of LIS ends with nums[i] 
        
        for i in range(len(nums)):
            LIS.append(1)
            for j in range(i):
                if nums[j] < nums[i]:
                    LIS[i] = max( LIS[i], LIS[j] + 1 )
        
        return max(LIS) if LIS else 0