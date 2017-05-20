class Solution(object):
    def intersect(self, nums1, nums2):
        
        def getCounts(nums):
            ret = dict()
            for num in nums:
                ret[num] = ret.get(num, 0) + 1
            return ret
        
        
        c1 = getCounts(nums1)
        c2 = getCounts(nums2)
        result = []
        for num in c1:
            if num in c2:
                for i in xrange(min(c1[num], c2[num])):
                    result.append(num)
        return result