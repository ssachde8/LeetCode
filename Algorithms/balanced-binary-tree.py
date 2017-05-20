# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    '''
    Check height of each subtree as we recurse down from the root.
    On each node, we recursively get the heights of left & right substrees. 
    If subtree is not balanced, then checkHeight will return the error code.
    The height of a null tree is defined as -1. Thus, use float(-inf) as error code
    '''
    def isBalanced(self, root):
        return self.checkHeight(root) != float("-inf")
        
    def checkHeight(self, root):
        if root is None: 
            return 0
        
        leftHeight = self.checkHeight(root.left)
        if leftHeight == float("-inf"): return float("-inf")  # pass error up
            
        rightHeight = self.checkHeight(root.right)
        if rightHeight == float("-inf"):    return float("-inf")  # pass error up
        
        # found error, pass it back
        if abs(leftHeight - rightHeight) > 1:   return float("-inf") 
        
        return max(leftHeight, rightHeight) + 1
        