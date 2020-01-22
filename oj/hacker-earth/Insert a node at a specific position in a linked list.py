import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node):
    while node:
        print(node.data)
        node = node.next


def insert_node_at_position(head, data, position):
    if head and data is not None and position is not None:

        index = 0

        c_node = head
        c_prev_node = None
        while c_node != None:
            if index == position:
                n = SinglyLinkedListNode(data)
                n.next = c_node

                if c_prev_node:
                    c_prev_node.next = n
                else:
                    head = n
                break

            index = index + 1
            c_prev_node = c_node
            c_node = c_node.next

    elif head is None:
        head = SinglyLinkedListNode(data)

    return head


def delete_node(head, position):
    if head:

        index = 0

        c_node = head
        c_prev_node = None
        while c_node:
            if index == position:
                if c_prev_node:
                    c_prev_node.next = c_node.next
                    c_node.next = None
                else:
                    head = head.next
            index = index + 1
            c_prev_node = c_node
            c_node = c_node.next
    return head


def reverse(head):
    if head and head.next:
        head.next.next = head
        head = None
        return head.next.next


def getNode(head, positionFromTail):
    if head:
        length = 0
        c_node = head
        while c_node:
            length = length+1
            c_node = c_node.next

        index_from_head = length - positionFromTail - 1

        if index_from_head >= 0:
            index = 0
            c_node = head
            while c_node:
                if index == index_from_head:
                    return c_node.data
                index = index + 1
                c_node = c_node.next
    return None


def compare_lists(head_one, head_two):
    if head_one and head_two:

        head_one_cur = head_one
        head_two_cur = head_two

        while head_one_cur and head_two_cur:
            if head_one_cur.data != head_two_cur.data:
                return 0
            head_one_cur = head_one_cur.next
            head_two_cur = head_two_cur.next

        if (head_one_cur and not head_two_cur) or (head_two_cur and not head_one_cur):
            return 0
        return 1
    return 0


# issue!
def mergeLists(head_one, head_two):
    if head_one and head_two:

        head_one_cur = head_one
        head_one_prev = None
        head_two_cur = head_two

        while head_one_cur and head_two_cur:
            if head_two_cur.data > head_one_cur.data:
                head_one_prev = head_one_cur
                head_one_cur = head_one_cur.next
            else:
                tmp_head_two_node = head_two_cur.next

                if head_one_prev:
                    head_one_prev.next = head_two_cur
                else:
                    head_two_cur.next = head_one
                    head_one = head_two_cur

                head_two_cur = tmp_head_two_node

        if head_two_cur and not head_one_cur and head_one_prev:
            head_one_prev.next = head_two_cur
    return head_one


if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    print()

    llist_2_count = int(input())

    l_2_list = SinglyLinkedList()

    for _ in range(llist_2_count):
        q = int(input())
        l_2_list.insert_node(q)

    print()

    # data = int(input())

    # position = int(input())

    # print()
    # print_singly_linked_list(llist.head)

    # llist_head = insert_node_at_position(llist.head, data, position)

    # print()
    # print_singly_linked_list(llist_head)

    # print()
    # head = delete_node(llist.head, int(input()))

    # print()
    # print_singly_linked_list(head)

    # print(getNode(llist.head, int(input())))

    # print_singly_linked_list(llist.head)
    # print_singly_linked_list(l_2_list.head)

    print()

    print_singly_linked_list(mergeLists(llist.head, l_2_list.head))
