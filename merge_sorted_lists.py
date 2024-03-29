"""
Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.
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
        print(node.data)
        while node.next != None:
            node = node.next
            print(node.data)

def merge_lists(LL1, LL2):
    ret = LinkedList()
    first_node = LL1.head
    second_node = LL2.head

    # Refactor
    while first_node != None and second_node != None:
        if first_node.data < second_node.data:
            ret.add_node(first_node)
            first_node = first_node.next
        else:
            ret.add_node(second_node)
            second_node = second_node.next

    while first_node != None:
        ret.add_node(first_node)
        first_node = first_node.next

    while second_node != None:
        ret.add_node(second_node)
        second_node = second_node.next

    # Pre Refactor
    # while first_node.next != None:
    #     if second_node.next == None:
    #         ret.add_node(first_node)
    #         first_node = first_node.next
    #     if first_node.data < second_node.data:
    #         ret.add_node(first_node)
    #         first_node = first_node.next
    #     else:
    #         ret.add_node(second_node)
    #         second_node = second_node.next
    #
    # while second_node.next != None:
    #     if first_node.next == None:
    #         ret.add_node(second_node)
    #         second_node = second_node.next
    #     if second_node.data < first_node.data:
    #         ret.add_node(second_node)
    #         second_node = second_node.next
    #     else:
    #         ret.add_node(first_node)
    #         first_node = first_node.next
    #
    # if first_node != None:
    #     ret.add_node(first_node)
    # if second_node != None:
    #     ret.add_node(second_node)

    return ret


LL1 = LinkedList()
LL1.add_node(Node(1))
LL1.add_node(Node(2))
LL1.add_node(Node(4))
LL1.add_node(Node(7))
LL1.add_node(Node(9))
# LL1.print_LL()

LL2 = LinkedList()
LL2.add_node(Node(1))
LL2.add_node(Node(3))
LL2.add_node(Node(4))
LL1.add_node(Node(8))
LL1.add_node(Node(20))
LL1.add_node(Node(21))
LL1.add_node(Node(22))
# LL2.print_LL()

test = merge_lists(LL1, LL2)
test.print_LL()
