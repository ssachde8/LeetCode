class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Beats 58%
        return (sum(set(nums))*2 - sum(nums))
        
        
        # XOR Operation
        # Run time : O(n) Space : O(1)
        # Beats 93%
        if not nums or len(nums) == 0:
            return 0
        x = 0
        for i in nums:
            x ^= i
        return x
        
        
        # Using Hash Table. Beats 56 %
        # Run Time : O(n) Space: O(n)
        lookup = set()
        for num in nums:
            if num in lookup:
                lookup.remove(num)
                continue
            lookup.add(num)
        return lookup.pop()
        
        
        # Beats 36%. O(nlogn)
        nums = sorted(nums)
        # print("Sorted:", nums)
        if len(nums) == 1:
            return nums[0]
        lookup = {}
        # cnt = collections.Counter(nums)
        for i in range(0,len(nums), 2):
            # print(i, nums[i], nums[i+1])
            if i+1 == len(nums):
                return nums[i]
            if nums[i] != nums[i+1]:
                return nums[i]
            
        