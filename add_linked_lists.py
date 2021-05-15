"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""

# Create a LL node and LL class
# Add func with two LL params
# Create result variable
# Keep track of current "node index"
# Traverse two LL's, add two values together, multiply by !0^node index, adding to result
# One we reach end of one linked list, travers remaining nodes of other list, do the add method described above

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

def sum_two_LL(LL1, LL2):
    ret = 0
    current_node1 = LL1.head
    current_node2 = LL2.head
    current_magnitude = 0
    while current_node1 != None and current_node2 != None:
        sum = (current_node1.data + current_node2.data) * (10**current_magnitude)
        ret += sum
        current_magnitude += 1
        current_node1 = current_node1.next
        current_node2 = current_node2.next
    if current_node1 != None:
        sum = current_node1.data * (10**current_magnitude)
        ret += sum
        current_magnitude += 1
        current_node1 = current_node1.next
    if current_node2 != None:
        sum = current_node2.data * (10**current_magnitude)
        ret += sum
        current_magnitude += 1
        current_node2 = current_node2.next
    return ret

LL1 = LinkedList()
LL1.add_node(Node(2))
LL1.add_node(Node(4))
LL1.add_node(Node(3))

LL2 = LinkedList()
LL2.add_node(Node(5))
LL2.add_node(Node(6))
LL2.add_node(Node(4))

print(sum_two_LL(LL1, LL2))

LL3 = LinkedList()
LL3.add_node(Node(9))
LL3.add_node(Node(9))
LL3.add_node(Node(9))
LL3.add_node(Node(9))
LL3.add_node(Node(9))
LL3.add_node(Node(9))
LL3.add_node(Node(9))

LL4 = LinkedList()
LL4.add_node(Node(9))
LL4.add_node(Node(9))
LL4.add_node(Node(9))
LL4.add_node(Node(9))

print(sum_two_LL(LL3, LL4))
