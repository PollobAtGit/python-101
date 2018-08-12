# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        if head:

            forward_pointer = head
            previous_pointer = None

            while forward_pointer:
                
                if forward_pointer.val == val:
                    if forward_pointer == head:
                        head = forward_pointer.next
                    else:
                        previous_pointer.next = forward_pointer.next
                else:
                    previous_pointer = forward_pointer

                forward_pointer = forward_pointer.next

        return head

    def iterate_through_list(self, head):

        if head:

            ret = []

            while head:
                ret.append(head.val)
                head = head.next

            return ret

        

s = Solution()

n_o = ListNode(22)
n_t = ListNode(25)
n_th = ListNode(60)
n_f = ListNode(70)
n_fi = ListNode(80)
n_s = ListNode(90)
n_se = ListNode(30)
n_e = ListNode(20)
# n_n = ListNode(90)


n_o.next = n_t
n_t.next = n_th
n_th.next = n_f
n_f.next = n_fi
n_fi.next = n_s
n_s.next = n_se
n_se.next = n_e
# n_e.next = n_n

print(s.iterate_through_list(s.removeElements(n_o, 40)))
# print(s.iterate_through_list(n_o))
