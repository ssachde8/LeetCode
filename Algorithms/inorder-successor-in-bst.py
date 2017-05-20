class Solution(object):
    def inorderSuccessor(self, root, p):
        '''
        Inorder traversal of bst returns nodes in ascending order.
        To find succ, we just need to find the smallest num which is larger than a given value since there are no duplicates in bst.
        Whenever we go left, the curr node becomes a possible succ else it stays the same.
        TIme: O(h), h is the depth of the result node
        '''
        # If it has right subtree, succ is the leftmost node of the right subtree
        if p and p.right:
            p = p.right # move to right subtree
            while p.left: # move to leftmost node
                p = p.left
            return p
            
        # search from root
        successor = None
        while root:
            if p.val < root.val: # node on left
                successor = root # possible succ
                root = root.left # traverse left
            else:
                root = root.right
        return successor
                