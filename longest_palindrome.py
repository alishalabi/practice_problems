"""
Given a string s, return the longest palindromic substring in s
"""

input1 = "babad"
input2 = "ac"
input3 = "zabcdefedcba"


def solution(string):
    output = ""
    for i in range(len(string)):
        longest = longest_palin(string, i)
        if len(longest) > len(output):
            output = longest
    return output


# TODO: Edge case: even lengthed palindrome
def longest_palin(string, index):
    longest = string[index]
    iterations = 1
    while index - iterations >= 0 and index + iterations < len(string):
        if string[index - iterations] == string[index + iterations]:
            longest = string[index - iterations] + longest + string[index + iterations]
        else:
            return longest
        iterations += 1
    return longest

# print(longest_palin(input1, 2))
print(solution(input1))
print(solution(input2))
print(solution(input3))
