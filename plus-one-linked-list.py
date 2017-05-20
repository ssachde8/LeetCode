# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        small_bit = None
        cur = head # cur has msb
        
        
        # example 1->2->9
        # STEP 1: store the final bit less than 9
        while cur:
            if cur.val < 9:
                small_bit = cur  # start = 2
            cur = cur.next # cur = 9
            
        # STEP 2: check if carry is needed
        #       : if small_bit: no carry, just add else: carry
        if small_bit:
            small_bit.val += 1  # 2 + 1 = 3
            cur = small_bit.next # cur = 9
        else: 
            # no small_bit. append carry bit to the head
            new_bit = ListNode(1) # carry bit
            new_bit.next = head # new_bit = 1
            cur = head # cur = 1
            head = new_bit # head poits to new_bit
            
        while cur: # cur = 1
            cur.val = 0 # cur = 0
            cur = cur.next # cur = None
            
        return head
                