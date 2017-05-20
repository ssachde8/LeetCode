class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # use binary search
        
        left, right = 1, len(nums)-1
        
        while left <= right:
            mid = left + (right-left)/2
            # count all number in nums <= mid
            count = 0
            for num in nums:
                if num <= mid:
                    count += 1
            
            # change search space using pigeonhole principle
            if count > mid: # duplicate element in [1 mid]
                right = mid - 1
            else:
                left = mid + 1 # duplicate element in [mid 1]
        return left