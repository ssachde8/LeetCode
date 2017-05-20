class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # work simplest case first
        #  f(–1) = f(0) = 0
        prev_max, cur_max = 0, 0
        for x in nums: # for each iteration cur_max becomes prev_max
            temp = cur_max
            cur_max = max( prev_max + x, cur_max )
            prev_max = temp
        return cur_max