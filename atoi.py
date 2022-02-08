"""
Your task  is to implement the function atoi. The function takes a string(str) as argument and converts it to an integer and returns it.

Note: You are not allowed to use inbuilt function.

Example 1:

Input:
str = 123
Output: 123
Example 2:

Input:
str = 21a
Output: -1
Explanation: Output is -1 as all
characters are not digit only.
Your Task:
Complete the function atoi() which takes a string as input parameter and returns integer value of it. if the input string is not a numerical string then returns -1.

Expected Time Complexity: O(|S|), |S| = length of string str.
Expected Auxiliary Space: O(1)
"""

def atoi(string):
    valid = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    ret = 0
    order = len(string) - 1
    remainder = string

    while len(remainder) != 0:
        if remainder[0] not in valid:
            return (-1)
        ret += int(remainder[0]) * (10**order)
        order -= 1
        remainder = remainder[1:]

    return ret



print(atoi("3217"))
