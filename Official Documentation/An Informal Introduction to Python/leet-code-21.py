def iterate(lst):
    y = []
    
    while lst is not None:
        y.append(lst.val)
        lst = lst.next

    return y

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return self.val

class Solution:

    # incomplete
    def mergeTwoLists_better(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 is None: return l2
        if l2 is None: return l1

        head = None
        m_l = None

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                
                if m_l is None:
                    m_l = l1
                    head = m_l
                else:
                    m_l.next = ListNode(l1.val)
                    m_l = m_l.next

                l1 = l1.next
            else:

                if m_l is None:
                    m_l = l2
                    head = m_l
                else:
                    m_l.next = ListNode(l2.val)
                    m_l = m_l.next

                l2 = l2.next
        
        if l1 is not None:
            while l1 is not None:

                m_l.next = ListNode(l1.val)
                m_l = m_l.next
                
                l1 = l1.next            
        elif l2 is not None:
            while l2 is not None:

                m_l.next = ListNode(l2.val)
                m_l = m_l.next
                
                l2 = l2.next

        return head
    
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 is None: return l2
        if l2 is None: return l1

        head = None
        m_l = None

        l_o_p = l1
        l_t_p = l2

        while l_o_p is not None and l_t_p is not None:
            if l_o_p.val < l_t_p.val:
                
                if m_l is None:
                    m_l = ListNode(l_o_p.val)
                    head = m_l
                else:
                    m_l.next = ListNode(l_o_p.val)
                    m_l = m_l.next

                l_o_p = l_o_p.next
            else:

                if m_l is None:
                    m_l = ListNode(l_t_p.val)
                    head = m_l
                else:
                    m_l.next = ListNode(l_t_p.val)
                    m_l = m_l.next

                l_t_p = l_t_p.next
        
        if l_o_p is not None:
            while l_o_p is not None:

                m_l.next = ListNode(l_o_p.val)
                m_l = m_l.next
                
                l_o_p = l_o_p.next            
        elif l_t_p is not None:
            while l_t_p is not None:

                m_l.next = ListNode(l_t_p.val)
                m_l = m_l.next
                
                l_t_p = l_t_p.next

        return head

    def mergeTwoLists_only_list(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        m_l = []

        l_o_p = 0
        l_t_p = 0

        while l_o_p < len(l1) and l_t_p < len (l2):
            if l1[l_o_p] < l2[l_t_p]:
                m_l.append(l1[l_o_p])
                l_o_p += 1
            else:
                m_l.append(l2[l_t_p])
                l_t_p += 1

        if l_o_p < len(l1):
            m_l += l1[l_o_p:]
        elif l_t_p < len(l2):
            m_l += l2[l_t_p:]

        return m_l

s = Solution()

# print(s.mergeTwoLists_only_list([7, 20, 99], [10, 13, 40]))
# print(s.mergeTwoLists_only_list([7, 20, 99, 100], [10, 13, 40, 80, 85, 89]))

l_h = ListNode(7)
l_h.next = ListNode(20)
l_h.next.next = ListNode(99)
l_h.next.next.next = ListNode(100)

r_h = ListNode(10)
r_h.next = ListNode(13)
r_h.next.next = ListNode(40)
r_h.next.next.next = ListNode(80)
r_h.next.next.next.next = ListNode(85)
r_h.next.next.next.next.next = ListNode(89)

# print(list(map(lambda x: x.val, s.mergeTwoLists(l_h, r_h))))
lst = s.mergeTwoLists(l_h, r_h)
# print(iterate(lst))

lst = s.mergeTwoLists(None, ListNode(0))
# print(iterate(lst))

print(iterate(s.mergeTwoLists_better(l_h, r_h)))
print(iterate(s.mergeTwoLists_better(None, ListNode(0))))
