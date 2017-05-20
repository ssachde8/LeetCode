# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result, path = [], []
        if root: 
            self.dfs(root, path, result)
        return result
        
    
    def dfs(self, root, path, result): # path maintains all nodes in a path
        if root.left is root.right is None: # leaf
            ans = ""
            for node in path:
                ans += str(node.val) + "->"
            result.append(ans + str(root.val))
            
        if root.left:
            path.append(root)
            self.dfs(root.left, path, result)
            path.pop()
            
        if root.right:
            path.append(root)
            self.dfs(root.right, path, result)
            path.pop()
        
        