class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        Scan the array from 0 to n-1. We store indices of promising elementes in dq.
        For each i,
        - Pop(end) indexes of smaller elements(useless)
        - Append current index
        - Pop(front) the index (i-k), if its still in dq.
        - If window has reached size k, append cur_max to output
        """ 
        
        dq = collections.deque() # stores indices
        out = []
        
        for i, num in enumerate(nums):
            # if cur>rear, pop rear
            while dq and nums[dq[-1]] < num: 
                dq.pop() 
            
            # append the current index
            dq.append(i)
            
            # if index (i-k) still in window, pop it, because it falls out of new win
            if dq[0] == i - k: 
                dq.popleft() # remove from front
            
            # if window has reached size k, append cur maximum
            if i + 1 >= k:    
                out.append( nums[ dq[0] ] )
        
        return out