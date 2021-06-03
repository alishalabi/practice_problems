"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at
coordinate (i, ai). n vertical lines are drawn such that the two endpoints of the
line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis
forms a container, such that the container contains the most water.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Example 3:
Input: height = [4,3,2,1,4]
Output: 16

Example 4:
Input: height = [1,2,1]
Output: 2
"""



input1 = [1,8,6,2,5,4,8,3,7]
input2 = [1,1]
input3 = [4,3,2,1,4]
input4 = [1,2,1]

# Brute force method: O(n)^2
def solution1(input):
    output = 0
    for i in range(len(input)):
        for j in (range(i, len(input))):
            min_height = min(input[i], input[j])
            area = min_height * (j - i)
            if area > output:
                output = area
    return output

# Two pointers method: O(n)
def solution2(input):
    left = 0
    right = len(input) - 1
    output = 0
    while left < right:
        area = min(input[left], input[right]) * (right - left)
        if area > output:
            output = area
        if input[left] < input[right]:
            left += 1
        else:
            right -= 1
    return output

# print(solution1(input1))
# print(solution1(input2))
# print(solution1(input3))
# print(solution1(input4))
print(solution2(input1))
print(solution2(input2))
print(solution2(input3))
print(solution2(input4))
