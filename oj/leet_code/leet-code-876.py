
# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head:

            l = 0

            each_itr_pointer = head
            half_itr_pointer = head

            while each_itr_pointer:
                l = l + 1

                if l % 2 == 0:
                    half_itr_pointer = half_itr_pointer.next

                each_itr_pointer = each_itr_pointer.next

            return half_itr_pointer


n_o = ListNode(10)
n_t = ListNode(20)
n_th = ListNode(30)
n_f = ListNode(40)
n_fi = ListNode(50)
n_s = ListNode(60)
n_se = ListNode(70)
n_e = ListNode(80)
# n_n = ListNode(90)


n_o.next = n_t
n_t.next = n_th
n_th.next = n_f
n_f.next = n_fi
n_fi.next = n_s
n_s.next = n_se
n_se.next = n_e
# n_e.next = n_n

s = Solution()

print(s.middleNode(n_o).val)

print(s.middleNode(ListNode(10)).val)

print(s.middleNode(n_e).val)
print(s.middleNode(n_se).val)


print(s.middleNode(n_s).val)


