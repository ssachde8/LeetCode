# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        if node and node.next: # node.next takes care of tail condition
            node_to_del = node.next
            node.val = node_to_del.val # copy next nodes val into current node
            node.next = node_to_del.next 
            del node_to_del