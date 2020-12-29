"""Introduction
Given a string of digits, calculate the largest product for a contiguous substring of digits of length n.

For example, for the input '1027839564', the largest product for a series of 3 digits is 270 (9 * 5 * 6), and the largest product for a series of 5 digits is 7560 (7 * 8 * 3 * 9 * 5).

Note that these series are only required to occupy adjacent positions in the input; the digits need not be numerically consecutive.

For the input '73167176531330624919225119674426574742355349194934', the largest product for a series of 6 digits is 23520.
"""

sample_input1 = "1027839564"
sample_input2 = "73167176531330624919225119674426574742355349194934"


def get_largest_series(string, length):
    if length > len(string):
        print("Error: substring is longer than string")
        return
    largest = 0
    for index in range(len(string) - 1 - length):
        single_value = 1
        counter = length
        while counter > 0:
            last_index = index + counter
            single_value = single_value * int(string[last_index])
            counter -= 1
        if single_value > largest:
            largest = single_value
    return largest


print(get_largest_series(sample_input1, 3))
print(get_largest_series(sample_input1, 5))
print(get_largest_series(sample_input2, 6))

print(get_largest_series(sample_input1, 300))
