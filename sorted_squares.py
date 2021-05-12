"""
Given an array of sorted integers, return a sorted array of those integers' squares.

Ex: [1, 2, 3] => [1, 4, 9]
Ex: [-12, 1, 2, 3] => [1, 4, 9, 144]
"""

# Step one: create sub arrays of all neg integers and pos ints, square both
# Step two: reverse order of negative array
# Step three: create output array, compare each element of two sub arrays

sample = [-12, -4, 0, 1, 2, 3, 9, 12]

def sorted_squares(sorted_input):
    neg_ints = []
    pos_ints = []
    result = []
    for int in sorted_input: # Time: O(n) where n is number of ints in input
        if int <= 0: # Cover zero in one case or the other
            neg_ints.insert(0, int**2)
        else:
            pos_ints.append(int**2)
    neg_index = 0
    pos_index = 0
    # Time: O(j) + O(k) => O(n), where j is number of pos ints and k is number of neg ints, always equals n
    while neg_index < len(neg_ints) and pos_index < len(pos_ints): # There are still items in both arrays
        if neg_ints[neg_index] < pos_ints[pos_index]:
            result.append(neg_ints[neg_index])
            neg_index += 1
        else:
            result.append(pos_ints[pos_index])
            pos_index += 1
    if neg_index < len(neg_ints):
        for i in range(neg_index, len(neg_ints)):
            result.append(neg_ints[i])
    if pos_index < len(pos_ints):
        for i in range(pos_index, len(pos_ints)):
            result.append(pos_ints[i])

    return result


print(sorted_squares(sample))
