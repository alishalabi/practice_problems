"""
Introduction
Implement encoding and decoding for the rail fence cipher.

The Rail Fence cipher is a form of transposition cipher that gets its name from the way in which it's encoded. It was already used by the ancient Greeks.

In the Rail Fence cipher, the message is written downwards on successive "rails" of an imaginary fence, then moving up when we get to the bottom (like a zig-zag). Finally the message is then read off in rows.

For example, using three "rails" and the message "WE ARE DISCOVERED FLEE AT ONCE", the cipherer writes out:

W . . . E . . . C . . . R . . . L . . . T . . . E
. E . R . D . S . O . E . E . F . E . A . O . C .
. . A . . . I . . . V . . . D . . . E . . . N . .
Then reads off:

WECRLTEERDSOEEFEAOCAIVDEN
To decrypt a message you take the zig-zag shape and fill the ciphertext along the rows.

? . . . ? . . . ? . . . ? . . . ? . . . ? . . . ?
. ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? .
. . ? . . . ? . . . ? . . . ? . . . ? . . . ? . .
The first row has seven spots that can be filled with "WECRLTE".

W . . . E . . . C . . . R . . . L . . . T . . . E
. ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? . ? .
. . ? . . . ? . . . ? . . . ? . . . ? . . . ? . .
Now the 2nd row takes "ERDSOEEFEAOC".

W . . . E . . . C . . . R . . . L . . . T . . . E
. E . R . D . S . O . E . E . F . E . A . O . C .
. . ? . . . ? . . . ? . . . ? . . . ? . . . ? . .
Leaving "AIVDEN" for the last row.

W . . . E . . . C . . . R . . . L . . . T . . . E
. E . R . D . S . O . E . E . F . E . A . O . C .
. . A . . . I . . . V . . . D . . . E . . . N . .
If you now read along the zig-zag shape you can read the original message.
"""

# Theory inspired by AllTech's Youtube Channel

from pprint import pprint
# Decoded: "WE ARE DISCOVERED FLEE AT ONCE"
# Encoded: "WECRLTEERDSOEEFEAOCAIVDEN"

sample_decoded = "WE ARE DISCOVERED FLEE AT ONCE"
sample_encoded = "WECRLTEERDSOEEFEAOCAIVDEN"

def clean_decoded(decoded_msg):
    ret = ""
    for letter in decoded_msg:
        if letter != " ":
            ret += letter
    return ret

def encode(decoded_msg, key):
    cleaned_decoded = str(clean_decoded(decoded_msg))
    row_direction = 1
    row = 0
    column = 0

    matrix = [["" for i in range(len(cleaned_decoded))]
                    for j in range(key)]

    for letter in cleaned_decoded:
        if row + row_direction < 0 or row + row_direction >= (key):
            row_direction = row_direction *- 1
        matrix[row][column] = letter
        column += 1
        row += row_direction

    # print(matrix)
    ret = ""
    for line in matrix:
        ret += "".join(line)
    return ret


def decode(encoded_msg):
    # line1 = ""
    # line2 = ""
    # line3 = ""
    # for letter in encoded_msg:
    #     if encoded_msg.index(letter) == 0:
    #         line1 += letter
    #     elif encoded_msg.index(letter) % 4 == 0:
    #         line1 += letter
    # print(line1)
    pass


print(encode(sample_decoded, 3))
