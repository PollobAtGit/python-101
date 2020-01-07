# 1
#   \
#    2--->3--->NULL
#   /
#  1

# 1--->2
#       \
#        3--->Null
#       /
#      1

# 2
# 3

# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def findMergeNode(head_o, head_t):
    if head_o is not None and head_t is not None:
        cur = head_o
        while cur:
            merge_d = None
            mid_cur = head_t
            while mid_cur:
                if mid_cur == cur:
                    merge_d = mid_cur.data
                    break
                mid_cur = mid_cur.next
            if merge_d is not None:
                return merge_d
            cur = cur.next

def length(head):
    if head is not None:
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        return length

def move_forward(itr, head):
    if head is not None:
        cur = head
        while cur:
            if itr == 0:
                return cur
            itr -= 1
            cur = cur.next

def find_merge_node(head_o, head_t):
    if head_o is not None and head_t is not None:
        
        head_o_len = length(head_o)
        head_t_len = length(head_t)

        if head_o_len > head_t_len:
            head_o = move_forward(head_o_len - head_t_len, head_o)
        elif head_t_len > head_o_len:
            head_t = move_forward(head_t_len - head_o_len, head_t)

        while head_o and head_t:
            if head_o == head_t:
                return head_o.data
            head_o = head_o.next
            head_t = head_t.next

