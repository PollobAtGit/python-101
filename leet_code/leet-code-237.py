# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        if node.next is not None:
            node.val = node.next.val
            
            t_h = node
            f_h = node.next
            
            while f_h.next is not None:
                f_h.val = f_h.next.val
                t_h = f_h
                f_h = f_h.next
            
            t_h.next = None