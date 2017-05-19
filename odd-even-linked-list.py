# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # odd and head are tail and head pointers for odd list
        # even and even_head are tail and head pointers for even list
        if head:
            odd = head
            even = head.next
            even_head = even
            while even and even.next:
                odd.next = even.next
                odd = odd.next
                even.next = odd.next
                even = even.next
                
            odd.next = even_head
            return head