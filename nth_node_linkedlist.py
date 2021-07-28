"""
Given the head of a linked list, remove the nth node from the end of the list
and return its head.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_node(self, node):
        if self.head == None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node
        self.length += 1

    def remove_nth1(position):
        target = self.length

nodeA = Node(1)
nodeB = Node(2)
nodeC = Node(3)
nodeD = Node(4)
nodeE = Node(5)

LL1 = LinkedList()
LL1.add_node(nodeA)
LL1.add_node(nodeB)
LL1.add_node(nodeC)
LL1.add_node(nodeD)
LL1.add_node(nodeE)

print(LL1.head.data)
print(LL1.tail.data)
print(LL1.length)
