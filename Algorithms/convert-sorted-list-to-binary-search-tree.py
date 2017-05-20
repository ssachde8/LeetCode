# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # nlogn
        if not head: return None
        if not head.next: return TreeNode(head.val)
        
        slow = head
        fast = head.next.next
        
        # slow reaches to root - 1 element
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # temp points to root
        temp = slow.next
        
        # cut down the left child
        slow.next = None
        
        root = TreeNode(temp.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(temp.next) # temp points to root
        
        
        return root
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        