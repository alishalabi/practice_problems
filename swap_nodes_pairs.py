"""
Given a linked list, swap every two adjacent nodes and return its head.
You must solve the problem without modifying the values in the list's nodes
(i.e., only nodes themselves may be changed.)


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]

"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
            return
        else:
            self.tail.next = node
            self.tail = node

    def print_LL(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.next


LL = LinkedList()
LL.add_node(Node(1))
LL.add_node(Node(2))
LL.add_node(Node(3))
LL.add_node(Node(4))

LL.print_LL()
