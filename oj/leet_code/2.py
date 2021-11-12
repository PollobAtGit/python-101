class Solution(object):
    def addTwoNumbers(self, l1, l2):

        arr_one = []
        arr_two = []

        while l1 or l2:
            if l1:
                arr_one.append(l1.val)
                l1 = l1.next
            if l2:
                arr_two.append(l2.val)
                l2 = l2.next

        arr_one.reverse()
        arr_two.reverse()
        
        i = len(arr_one) - 1
        j = len(arr_two) - 1

        arr_sum = []
        carry = 0

        while i >= 0 or j >= 0:
            v = arr_one[i] if i < len(arr_one) and i >= 0 else 0
            q = arr_two[j] if j < len(arr_two) and j >= 0  else 0

            sum = v + q + carry

            carry = 1 if sum >= 10 else 0
            arr_sum.append(sum - 10 if sum >= 10 else sum)

            i = i - 1
            j = j - 1

        if carry == 1:
            arr_sum.append(carry)
        
        h = ListNode()
        itr = h

        for i in range(len(arr_sum)):
            v = ListNode()
            v.val = arr_sum[i]
            itr.next = v
            itr = v

        return h.next

