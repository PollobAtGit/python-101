# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        return str(self.val)

class Solution:
    def isPalindrome(self, head):
        if head is not None:

            stack = []
            i = 0
            jumping_head = head

            while jumping_head:
                
                jumping_head = jumping_head.next

                if jumping_head:
                    i = i + 1
                    jumping_head = jumping_head.next

                    if jumping_head:
                        i = i + 1                    

                stack.append(head.val)
                head = head.next

            if i % 2 == 0 and stack:
                stack.pop()

            while head:
                if stack and stack.pop() != head.val:
                    return False
                head = head.next

            return True if not stack else False
        else:
            return True


'''
    print(stack)
    print("i: ", i)
    print(head.val)



    print(stack)
'''

a = ListNode(1)
b = ListNode(0)
c = ListNode(1)
d = ListNode(1)

a.next = b
b.next = c
c.next = d

s = Solution()
print(s.isPalindrome(a))

