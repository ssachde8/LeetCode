# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Merge Sort Implementation
        if head == None or head.next == None: return head
        
        # STEP 1 : Cut the list in 2 halves
        fast, slow, prev = head, head, None
        
        while fast and fast.next: # slow reaches to middle
            prev, fast, slow = slow, fast.next.next, slow.next
        prev.next = None
            
        # STEP 2: Sort each half
        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        
        # STEP 3: Merge l1 and l2
        return self.mergeTwoLists(l1, l2)
        
        
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next, cur, l1 = l1, l1, l1.next
            else:
                cur.next, cur, l2 = l2, l2, l2.next
                
        cur.next = l1 or l2
        
        return dummy.next
        
        
        
        