# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
    
        # in postorder, root is visited last
        root = TreeNode(postorder.pop())
        root_pos = inorder.index(root.val)
        
        root.right = self.buildTree(inorder[root_pos+1:], postorder)
        root.left = self.buildTree(inorder[:root_pos], postorder)
        return root