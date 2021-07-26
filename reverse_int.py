"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
Example 4:

Input: x = 0
Output: 0
"""

input1 = 123
input2 = -123
input3 = 120

def reverse(input):
    if input < 0:
        string_input = str(-input)
    else:
        string_input = str(input)
    output = ""
    for i in range(len(string_input)):
        output = string_input[i] + output
    if input < 0:
        return (-int(output))
    else:
        return (int(output))


print(reverse(input1))
print(reverse(input2))
print(reverse(input3))
