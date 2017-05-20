class Solution(object):
    def twoSum(self, nums, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
            
        lookup = {}
        for i,num in enumerate(nums):
            if target-num in lookup:
                return lookup[target-num]+1, i+1
            else:
                lookup[num] = i