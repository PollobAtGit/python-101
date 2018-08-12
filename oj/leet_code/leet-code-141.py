# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    
    def two_pointer_solution(self, head):

        if head:

            if head.next is None: 
                return False

            current_head = head.next
            back_runner = head

            iteration = 1

            while current_head and back_runner and current_head != back_runner:

                if iteration % 2 == 0:
                    back_runner = back_runner.next

                iteration = iteration + 1
                current_head = current_head.next

            if current_head == back_runner:
                return True
            return False

        return False
        

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if head:

            traversed_nodes = set()

            current_head = head

            while current_head:

                if current_head not in traversed_nodes:
                    traversed_nodes.add(current_head)
                else:
                    return True

                current_head = current_head.next

            return False
        return False

s = Solution()

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
n_f.next = n_o
n_fi.next = n_s
n_s.next = n_se
n_se.next = n_e
# n_e.next = n_n


print(s.hasCycle(n_o))
print(s.two_pointer_solution(n_o))
print(s.two_pointer_solution(None))

