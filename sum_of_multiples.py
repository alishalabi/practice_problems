"""
Given a number, find the sum of all the unique multiples of particular numbers
up to but not including that number.

If we list all the natural numbers below 20 that are multiples of 3 or 5, we get
3, 5, 6, 9, 10, 12, 15, and 18.

The sum of these multiples is 78.

You can make the following assumptions about the inputs to the sum_of_multiples
function:

All input numbers are non-negative ints, i.e. natural numbers including zero.
A list of factors must be given, and its elements are unique and sorted in
ascending order.
"""

target = 20
multiples = [3, 5]

# def sum_of_multiples(target, multiples):
#     output = []
#     for multiple in multiples:
#         for number in range(target):
#             if number % multiple == 0 and number not in output:
#                 output.append(number)
#     return sum(output)

def sum_of_multiples(target, multiples):
    seen = set()
    output = 0
    for multiple in multiples:
        for number in range(target):
            if number % multiple == 0 and number not in seen:
                seen.add(number)
                output += number
    return output

print(sum_of_multiples(target, multiples))
