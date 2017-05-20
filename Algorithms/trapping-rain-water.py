class Solution(object):
    def trap(self, H):
        """
        :type height: List[int]
        :rtype: int
        """
        a, b = 0, len(H)-1 # a and b are left and right pointers
        leftMax, rightMax = 0, 0 # maximum height from forward and backward direction
        res = 0
        while a <= b:
            
            leftMax = max( leftMax, H[a] ) # max height seen on left
            rightMax = max( rightMax, H[b] ) # max height seen on right
            
            # store rain water -> max - curHeight
            if leftMax <= rightMax: 
                res += (leftMax - H[a]) 
                a += 1
            else:
                res += (rightMax - H[b])
                b -= 1
        return res
    