class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        cur_sum = 0
        for num in nums:
            cur_sum += num
            if cur_sum > max_sum: max_sum = cur_sum
            if cur_sum < 0: cur_sum = 0 # cannot go back and make the val positive
        return max_sum