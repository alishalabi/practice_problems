"""
Introduction
Implement a doubly linked list.

Like an array, a linked list is a simple linear data structure. Several common data types can be implemented using linked lists, like queues, stacks, and associative arrays.

A linked list is a collection of data elements called nodes. In a singly linked list each node holds a value and a link to the next node. In a doubly linked list each node also holds a link to the previous node.

You will write an implementation of a doubly linked list. Implement a Node to hold a value and pointers to the next and previous nodes. Then implement a List which holds references to the first and last node and offers an array-like interface for adding and removing items:

push (insert value at back);
pop (remove value at back);
shift (remove value at front).
unshift (insert value at front);
To keep your implementation simple, the tests will not cover error conditions. Specifically: pop or shift will never be called on an empty list.
"""


class Node:
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.previous = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.tail == None:
            print("Error: cannot pop from an empty linked list")
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.previous

    def shift(self):
        if self.tail == None:
            print("Error: cannot pop from an empty linked list")
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

    def unshift(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.previous = new_node
            self.head = new_node


# LL = LinkedList()
# LL.push("Apple")
# print(LL.head.data)
# print(LL.tail.data)
# LL.push("Banana")
# print(LL.head.data)
# print(LL.tail.data)
# LL.push("Cherry")
# print(LL.head.data)
# print(LL.head.next.data)
# print(LL.tail.data)
# LL.pop()
# print(LL.head.data)
# print(LL.tail.data)
# LL.pop()
# LL.pop()
# LL.pop()
# LL.shift()
# print(LL.head.data)
# print(LL.tail.data)
# LL.unshift("Xenon")
# print(LL.head.data)
# print(LL.head.next.data)
# print(LL.tail.data)
