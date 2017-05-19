class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # beats 90%
        return len(nums) > len(set(nums))
        
        
        # beats 35%
        lookup = {}
        for i, num in enumerate(nums):
            if num not in lookup:
                lookup[num] = 1
            else:   # if element in lookup
                return True
        
        return False