# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
            
        a, b = headA, headB
        
        while a != b:
            a = (headB if a is None else a.next)
            b = (headA if b is None else b.next)
        return a
            