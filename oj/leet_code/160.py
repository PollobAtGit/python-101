# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):

    def getLength(this, head):
        if head:

            iterator = head
            length = 0

            while iterator:
                length += 1
                iterator = iterator.next

            return length

    def getIntersectionNode(self, headA, headB):
        if headA and headB:

            headOneLen = self.getLength(headA)
            headTwoLen = self.getLength(headB)

            if headOneLen > headTwoLen:
                diff = headOneLen - headTwoLen
                while diff:
                    headA = headA.next
                    diff -= 1
            else:
                diff = headTwoLen - headOneLen
                while diff:
                    headB = headB.next
                    diff -= 1

            while headA:
                if headA == headB:
                    return headA
                headA = headA.next
                headB = headB.next

            return None

    def getIntersectionNode(self, headA, headB):
        if headA and headB:
            iteratorA = headA
            while iteratorA:
                iteratorB = headB
                while iteratorB:
                    if iteratorA == iteratorB:
                        return iteratorB
                    iteratorB = iteratorB.next
                iteratorA = iteratorA.next

            return None
