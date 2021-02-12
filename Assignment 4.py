# Given two sorted lists of integers, write a function merge that merges the two lists and produces a new 
# sorted list. Either input list can be empty. Please write your own function for completing this, 
# rather than using any kind of sort or zip function built into the language. For example:

# A = [5, 10, 15, 20]
# B = [3, 7, 13, 60]
# C = merge(A, B)
# # C now equals [3, 5, 7, 10, 13, 15, 20, 60]

#############################################################################

# Given a singly linked list, write a function, reverse_print(l), that prints the values of each node of the list reverse order. For example, calling the function with the list 1 -> 2 -> 3 would print:

# 3
# 2
# 1

# You'll need to create your own linked list / node class for this problem and the next one. Keep it simple — remember linked list nodes are just a value and a pointer.
# Please write your own function for reversing the list, rather than any one built into the language.


#############################################################################
# Given a singly linked list, write a function, reverse(l), that returns a new linked list with the nodes 
# in reverse order. For example, calling the function with the list 1 -> 2 -> 3 would return the list 3 -> 2 -> 1.

# 3 2 1


#############################################################################

import pytest


def merge(a, b):
    ans = [None for _ in range(len(a) + len(b))]
    ans_idx = 0
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            ans[ans_idx] = a[i]
            i += 1
        else:
            ans[ans_idx] = b[j]
            j += 1
        ans_idx += 1
    if i < len(a):
        ans[ans_idx:] = a[i:]
    elif j < len(b):
        ans[ans_idx:] = b[j:]
    return ans


class Node:
  def __init__(self, data=None, next=None):
      self.data = data
      self.next = next


def reverse_print(x: Node) -> None:
    if not x:
        return
    reverse_print(x.next)
    print(x.data)


def reverse(x: Node) -> Node:
    dummy_head = Node(data=None)
    def helper(node):
        if not node:
            return dummy_head
        last_node = helper(node.next)
        last_node.next = node
        node.next = None
        return node
    helper(x)
    return dummy_head.next

