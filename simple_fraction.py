# INCOMPLETE

"""
Given a fraction. Convert it into a decimal.
If the fractional part is repeating, enclose the repeating part in parentheses.


Example 1:

Input: numerator = 1, denominator = 3
Output: "0.(3)"
Explanation: 1/3 = 0.3333... So here 3 is
recurring.
Example 2:

Input: numerator = 5, denominator = 2
Output: "2.5"
Explanation: 5/2 = 2.5
"""

def solve(num, denom):
    ret = ""
    left = num // denom
    right = ""
    remainder = num % denom
    if remainder == 0:
        return str(left)

    converted = remainder / denom
    print(converted)

    seen = {}

    while (converted != 0 and converted not in seen):
        seen.append(converted)





print(solve(5, 2))
