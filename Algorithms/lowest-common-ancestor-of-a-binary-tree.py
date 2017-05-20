# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        a, b = sorted([p.val, q.val])

        while not a <= root.val <= b:
            # Keep searching since root is outside of [a, b].
            if a <= root.val:
                root = root.left  
            else:
                root = root.right
        return root