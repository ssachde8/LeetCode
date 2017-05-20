class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        # beats 77%(xrange) 70% (range)
        pos = 0 
        for i in range(len(nums)):
            if nums[i]:
                nums[pos] = nums[i] # overwrite zeroes
                pos += 1
        
        for i in range(pos, len(nums)): # append zeroes at the end
            nums[i] = 0 
            
        
        '''
        # beats 13%
        for i, num in enumerate(nums):
            if num == 0:
                nums.remove(num)
                nums.append(num)
        '''
                