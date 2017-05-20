# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # Iterative. Level by level
    # traverse tree level by level 
    # add the last value of each level to the view
    def rightSideView(self,root):
        view = []
        if root:
            level = [root]
            while level:
                view += level[-1].val, # , end the line with no new line
                level = [child for node in level for child in (node.left,node.right) if child]
        return view