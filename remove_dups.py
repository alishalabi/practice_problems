"""
Given a sorted array nums, remove the duplicates in-place such that each element
appears only once and returns the new length.

Do not allocate extra space for another array, you must do this by modifying the
input array in-place with O(1) extra memory.

Ex 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2]

Ex 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
"""

sample = [0,0,1,1,1,2,2,3,3,4]

def solution(array):
    right = len(array) - 1
    while right > 0:
        if array[right] == array[right - 1]:
            array.pop(right)
        else:
            right -= 1
    print(array)
    return len(array)

print(solution(sample))
