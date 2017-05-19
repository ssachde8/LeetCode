class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # complexity nlogn
        # use radix sort or bucket sort for O(n)
        if len(nums) < 2: return 0
        nums = sorted(nums)
        maxDiff = 0
        for i in range(1, len(nums)):
            maxDiff = max(maxDiff , (nums[i] - nums[i-1]) )
            
        return maxDiff