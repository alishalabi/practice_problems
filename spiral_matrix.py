"""
Given the size, return a square matrix of numbers in spiral order.

The matrix should be filled with natural numbers, starting from 1 in the top-left
corner, increasing in an inward, clockwise spiral order, like these examples:

Spiral matrix of size 3
1 2 3
8 9 4
7 6 5
Spiral matrix of size 4
 1  2  3 4
12 13 14 5
11 16 15 6
10  9  8 7
"""

size = 3

def form_matrix(size):
    matrix = [[0 for x in range(size)] for y in range(size)]
    for digit in range(1, size ** 2 + 1):
        print(digit)

form_matrix(size)
