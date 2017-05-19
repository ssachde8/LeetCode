class Solution(object):
    def threeSum(self, num):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
        Fix first number. Second and third then can be found similr to in 2Sum.
        '''
        
        
        if len(num)<3: return []
        num.sort()
        res = []
        
        
        for i in range(len(num)-2): 
            left = i + 1
            right = len(num) - 1
            if i!=0 and num[i] == num[i-1]: 
                continue
            while left < right:
                
                if num[left] + num[right] + num[i] == 0:
                    res.append([num[i], num[left], num[right]])
                    left = left+1
                    right = right-1
                    
                    # avoid duplicates of first & second number
                    while num[left] == num[left-1] and left < right: left = left+1
                    while num[right] == num[right+1] and left < right:  right = right-1
                        
                        
                elif num[left] + num[right] + num[i] < 0:
                    left = left+1
                else:
                    right = right-1
        return res
                    