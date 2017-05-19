class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums: return []
        if len(nums) == 1: return [str(nums[0])]
        
        res = []
        head = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] > 1: # if difference is greater than 1
                if head == nums[i-1]:
                    s = str(head) 
                else: # adjacent numbers difference
                    s = str(head) + "->" + str(nums[i-1])
                res.append(s)
                head = nums[i]
                
            if i == len(nums)-1: # if second last num, for boundary case
                if head == nums[i]:
                    s = str(head)
                else:
                    s = str(head) + "->" + str(nums[i])
                res.append(s)
                
        return res