# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        
        # beats 99%
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
        
        # beats 23%
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left,right)+1
            