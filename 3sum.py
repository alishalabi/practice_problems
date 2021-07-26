"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

input = [-1, 2, 1, -4]
target = 1

# Sort array
# Set baseline output
# Iterate through each index (up until last 2)
# Instantiate two pointers (start and finish)
# Get sum of index and pointers
# If sum is exactly target, return
# If sum is less than target, increment finished down
# If sum is more than target, incremenet start up

def three_sum(input, target):
    sorted_input = sorted(input)
    sum = sorted_input[0] + sorted_input[1] + sorted_input[2]
    output = sum
    for i in range(len(sorted_input) - 2):
        start = i + 1
        finish = len(sorted_input) - 1

        while start < finish:
            new_sum = sorted_input[i] + sorted_input[start] + sorted_input[finish]
            if abs(new_sum - target) == 0:
                return new_sum
            elif abs(new_sum - target) < abs(output - target):
                output = new_sum
            if new_sum < target:
                start += 1
            elif new_sum > target:
                finish -= 1
    return output



print(three_sum(input, target))
