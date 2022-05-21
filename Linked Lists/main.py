class SinglyLinkedListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None


a = SinglyLinkedListNode(1)
b = SinglyLinkedListNode(2)
c = SinglyLinkedListNode(3)
a.next = b
b.next = c
print(a.data)
print(a.next.data)
print(a.next.next.data)


class DoublyLinkedListNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


a = DoublyLinkedListNode(1)
b = DoublyLinkedListNode(2)
c = DoublyLinkedListNode(3)
a.next = b
b.prev = a
b.next = c
c.prev = b
print(a.data)
print(a.next.data)
print(a.next.next.data)
print(c.data)
print(c.prev.data)
print(c.prev.prev.data)

# Singly Linked List Cycle Check
"""
Problem
Given a singly linked list, write a function which takes in the first node in a singly linked list and
returns a boolean indicating if the linked list contains a "cycle".

A cycle is when a node's next point actually points back to a previous node in the list. This is
also sometimes known as a circularly linked list.

You've been given the Linked List Node class code:
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def check_cycle(node):
    runner_1 = node
    runner_2 = node

    while runner_2 is not None and runner_2.next is not None:
        runner_1 = runner_1.next
        runner_2 = runner_2.next.next

        # Overlapping occurs
        if runner_1 == runner_2:
            return True

    return False


a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c
c.next = a # Cycle here!
print(check_cycle(a))

x = Node(1)
y = Node(2)
z = Node(3)
x.next = y
y.next = z
print(check_cycle(x))


# Linked List Reversal
"""
Problem
Write a function to reverse a Linked List in place. The function will take in the head of the list as input
and return the new head of the list.

You are given the example Linked List Node class:
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def reverse(h: Node) -> Node:
    prev = None
    curr = h
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
a.next = b
b.next = c
c.next = d
print(a.data, a.next.data, a.next.next.data, a.next.next.next.data)
head = reverse(a)
print(head.data, head.next.data, head.next.next.data, head.next.next.next.data)

# Linked List Nth to Last Node
"""
Problem Statement
Write a function that takes a head node and an integer value n and then returns the nth to last
node in the linked list. For example, given:
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)
e = Node(5)

a.next = b
b.next = c
c.next = d
d.next = e


# def nth_to_last_node(n, head):
#     new_head = reverse(head)
#     for i in range(n-1):
#         new_head = new_head.next
#     return new_head


def nth_to_last_node(n, head):
    first = head
    last = head

    # Move first n steps ahead of last
    for i in range(n):
        first = first.next

    while first:
        first = first.next
        last = last.next

    return last


# This would return the node d with a value of 4, because its the 2nd to last node.
target_node = nth_to_last_node(2, a)
print(target_node.data)
