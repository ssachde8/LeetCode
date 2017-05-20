class MinStack(object):


    """
    maintain min element at 
    """
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        min = self.getMin()
        if min is None or x < min:
            min = x
        self.stack.append(( x, min ))   # insert min at position x
        

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        return self.stack[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.stack) == 0:
            return None
        return self.stack[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()