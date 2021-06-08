"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

input = [3,2,4]

def solution(input, target):
    all_nums = set()
    for number in input:
        if number not in all_nums:
            all_nums.add(number)

    for i in range(len(input) - 1):
        compliment = target - input[i]
        if compliment in all_nums and i != input.index(compliment):
            return [i, input.index(compliment)]

print(solution(input, 6))
