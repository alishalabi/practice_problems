"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where
adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.


Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
"""

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

directions =[
    (0, -1),
    (1, 0),
    (0, 1),
    (-1, 0)
]

def dfs(board, row, column, word):
    print(word)
    if len(word) == 0:
        return True
    if row < 0 or row >= len(board) or column < 0 or column >= len(board[0]):
        # print("Off row or column")
        return False
    if board[row][column] != word[0]:
        # (print("Word not found"))
        return False

    temp = board[row][column]
    board[row][column] = " "

    for direction in directions:
        new_row = row + direction[0]
        new_column = column + direction[1]
        # print(f"Row: {new_row}")
        # print(f"Column: {new_column}")
        ret = dfs(board, row + direction[0], column + direction[1], word[1:])

    board[row][column] = temp
    return ret

def word_present(board, word):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if dfs(board, i, j, word):
                return True
    return False

print(word_present(board, word))
