class Solution(object):
    def countBits(self, num):
        res = [0]
        for i in range(1, num+1):
            # number of 1's in i = (i & 1) + number of 1's in (i / 2)
            res.append( (i & 1) + res[i >> 1] )
        return res