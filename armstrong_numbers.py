"""
Introduction
An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.

For example:

9 is an Armstrong number, because 9 = 9^1 = 9
10 is not an Armstrong number, because 10 != 1^2 + 0^2 = 1
153 is an Armstrong number, because: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
154 is not an Armstrong number, because: 154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190
Write some code to determine whether a number is an Armstrong number.
"""


def armstrong_number(input):
    string_input = str(input)
    armstrong_value = len(string_input)
    converted_sum = 0
    for digit in string_input:
        converted_sum += (int(digit) ** armstrong_value)
    if converted_sum == input:
        return True
    else:
        return False


print(armstrong_number(9))  # Should be true
print(armstrong_number(10))  # Should be false
print(armstrong_number(153))  # Should be true
print(armstrong_number(154))  # Should be false
