# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        vals = []   # hold list values
        while head: # traverse till end
            vals.append(head.val)
            head = head.next
        return vals == vals[::-1]   # compare list values with reverse list values
            
            
            
            
            