# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        return self.helper([], [], root, sum)
        
        
    def helper(self, result, cur, root, sum): # cur holds current result
        if root is None:
            return result
        
        if root.left is None and root.right is None and root.val == sum:
            result.append(cur + [root.val]) # correct sum found
            return result
            
        cur.append(root.val)
        self.helper(result, cur, root.left, sum-root.val)
        self.helper(result, cur, root.right, sum-root.val)
        cur.pop() # pop last added element to improve performance 5 fold
        return result
        