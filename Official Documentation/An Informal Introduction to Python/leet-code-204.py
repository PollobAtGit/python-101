# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    # solution not clear
    def reverseList(self, head):

        if head is None or head.next is None:
            return head

        d_h = head.next
        r = self.reverseList(head.next)
        head.next = None
        d_h.next = head
        
        return r
    
    def reverseList_r(self, head):

        if head is None: return None

        if head.next is None:
            return head

        r_head = self.reverseList_r(head.next)

        d_r_h = r_head

        while d_r_h.next is not None:
            d_r_h = d_r_h.next

        d_r_h.next = head
        head.next = None
        
        return r_head

    def reverseList_itr(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None: return None
        
        d_h = head
        lst = []

        while d_h is not None:
            lst.append(d_h.val)
            d_h = d_h.next
        
        if len(lst) != 0:
            lst = lst[::-1]
            r_head = ListNode(lst[0])
            d_h = r_head
            for x in lst[1:]:
                n = ListNode(x)
                d_h.next = n
                d_h = n
                
        return r_head
        
h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
h.next.next.next.next = ListNode(5)

def traverse(hd):
    r = []
    d_h = hd
    while d_h is not None:
        r.append(d_h.val)
        d_h = d_h.next
    return r

# print(traverse(h))

s = Solution()

"""
print(traverse(s.reverseList_r(h)))
print(traverse(s.reverseList_r(ListNode(2))))
print(traverse(s.reverseList_r(None)))

print(traverse(s.reverseList_r(h)))
"""

print(traverse(s.reverseList(h)))
print(traverse(s.reverseList(ListNode(2))))
print(traverse(s.reverseList(None)))

print(traverse(s.reverseList(h)))
