# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        cur = head
        # Step 1: make copy of each node and link
        # them together side by side in a single list
        while cur:
            copy = RandomListNode(cur.label)
            copy.next = cur.next # copy points to cur.next
            cur.next = copy # copy and cur get side by side
            cur = copy.next # skip copy
        
        # Step 2: Assign random pointers for the copy nodes
        cur = head
        while cur:
            if cur.random: # copy elements are skipped, since they dont have random
                cur.next.random = cur.random.next # copy.random = cur.r.next
            cur = cur.next.next # skip copy
        
        # Step 3: Restore the original list, and extract the copy list
        dummy = RandomListNode(0) # pseudohead
        cur_copy, cur = dummy, head
        while cur:
            cur_copy.next = cur.next
            cur.next = cur.next.next
            cur_copy, cur = cur_copy.next, cur.next
        return dummy.next