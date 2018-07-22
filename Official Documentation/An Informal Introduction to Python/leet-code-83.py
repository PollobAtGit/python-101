def iterate(lst):
    y = []
    
    while lst is not None:
        y.append(lst.val)
        lst = lst.next

    return y

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return self.val

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None or head.next is None: return head        

        d_h = head.next
        p_h = head

        while d_h is not None:

            has_changed = False
            while d_h is not None and p_h is not None and d_h.val == p_h.val:
                has_changed = True
                d_h = d_h.next
            
            if has_changed:
                p_h.next = d_h

            p_h = d_h
                
            if d_h is not None:
                d_h = d_h.next

        return head

r_h = ListNode(10)
r_h.next = ListNode(10)
r_h.next.next = ListNode(10)
r_h.next.next.next = ListNode(10)
r_h.next.next.next.next = ListNode(89)
r_h.next.next.next.next.next = ListNode(89)
r_h.next.next.next.next.next.next = ListNode(89)
r_h.next.next.next.next.next.next.next = ListNode(89)
            
s = Solution()
        
print(iterate(s.deleteDuplicates(r_h)))
print(iterate(s.deleteDuplicates(None)))
print(iterate(s.deleteDuplicates(ListNode(10))))
