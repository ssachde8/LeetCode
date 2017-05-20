# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None: return []
        result, current, level = [], [root], 1
        
        while current:
            next_level, values = [], []
            for node in current:
                values.append(node.val)
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            
            result.append(values) if level % 2 else result.append(values[::-1])
            level += 1
            current = next_level
        return result
                
            