"""
Introduction
A circular buffer, cyclic buffer or ring buffer is a data structure that uses a single, fixed-size buffer as if it were connected end-to-end.

A circular buffer first starts empty and of some predefined length. For example, this is a 7-element buffer:

[ ][ ][ ][ ][ ][ ][ ]
Assume that a 1 is written into the middle of the buffer (exact starting location does not matter in a circular buffer):

[ ][ ][ ][1][ ][ ][ ]
Then assume that two more elements are added — 2 & 3 — which get appended after the 1:

[ ][ ][ ][1][2][3][ ]
If two elements are then removed from the buffer, the oldest values inside the buffer are removed. The two elements removed, in this case, are 1 & 2, leaving the buffer with just a 3:

[ ][ ][ ][ ][ ][3][ ]
If the buffer has 7 elements then it is completely full:

[6][7][8][9][3][4][5]
When the buffer is full an error will be raised, alerting the client that further writes are blocked until a slot becomes free.

When the buffer is full, the client can opt to overwrite the oldest data with a forced write. In this case, two more elements — A & B — are added and they overwrite the 3 & 4:

[6][7][8][9][A][B][5]
3 & 4 have been replaced by A & B making 5 now the oldest data in the buffer. Finally, if two elements are removed then what would be returned is 5 & 6 yielding the buffer:

[ ][7][8][9][A][B][ ]
Because there is space available, if the client again uses overwrite to store C & D then the space where 5 & 6 were stored previously will be used not the location of 7 & 8. 7 is still the oldest element and the buffer is once again full.

[D][7][8][9][A][B][C]
"""

# Create node struct, create buffer struc
# Each node has a position and a piece of data

class BufferNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularBuffer:
    def __init__(self, max_length):
        self.max_length = max_length
        self.current_size = 0
        self.head = None
        self.tail = None

    def add_Node(self, data):
        # Case buffer too large
        if self.current_size >= self.max_length:
            print("Error: Circular buffer full! Remove a node before adding a new one")
            return
        new_node = BufferNode(data)
        # Case no data in buffer
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            self.current_size += 1
        # Case simple add
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.current_size += 1

    def remove_Node(self):
        # Case empty buffer
        if self.current_size <= 0:
            print("Error: Circular buffer empty! Add a node before removing one")
        # Case last node in buffer
        if self.current_size == 1:
            self.head = None
            self.tail = None
            self.current_size -= 1
        # Case simple remove
        else:
            new_head = self.head.next
            self.head = new_head
            self.current_size -= 1


test_buffer = CircularBuffer(3)
test_buffer.add_Node("A")
test_buffer.add_Node("B")
test_buffer.add_Node("C")
# print(test_buffer.head.data)
# print(test_buffer.head.next.data)
# print(test_buffer.tail.data)
# test_buffer.add_Node("D")
