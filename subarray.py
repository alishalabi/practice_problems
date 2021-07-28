"""
Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

"""

input = [-2,1,-3,4,-1,2,1,-5,4]

# def solution(input):
#     left = 0
#     right = len(input) - 1
#     output = sum(input)
#     print(output)
#     while left < right:
#         if input[left] < input[right]:
#             new_sum = output - input[left]
#             print(new_sum)
#             if new_sum > output:
#                 output = new_sum
#             left += 1
#         else:
#             new_sum = output - input[right]
#             print(new_sum)
#             if new_sum > output:
#                 output = new_sum
#
#             right -= 1
#     return output
#
# print(solution(input))

# TODO: Finish Kadam's solution

def solution(input):
    output = input[0]
    previous = input[0]
    for i in range(1, len(input) - 1):
        new_sum = previous + input[i]
        if new_sum > output:
            output = new_sum
            previous = new_sum
        else:
