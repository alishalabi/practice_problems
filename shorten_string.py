"""
Given a string and a set character limit, shorten a string
so that it is no longer than the set limit. Replace excess
characters with a '...' (not counted toward char limit),
with an equal number original charactersat the beginning
and end of the shortened string.
If you have an odd-numbered character limit, include one extra
character at the beginning of the shortened string.

Input: "What a beautiful day in the neighborhood", 12 characters
Output: "What a...orhood"

Input: "What a beautiful day in the neighborhood", 11 characters
Output: "What a...rhood"

Input: "Happy days yours and mine", 8 characters
Output: "Happ...mine"
"""


def shorten_string(original_string, char_limit):
    if len(original_string) + 1 < char_limit:
        return original_string
    first_string = ""
    second_string = ""
    current_index = 0
    if char_limit % 2 == 0:  # Even char limit
        while current_index < (char_limit / 2):
            first_string += original_string[current_index]
            second_string = original_string[-current_index - 1] + second_string
            current_index += 1
    elif char_limit % 2 == 1:
        adjusted_char_limit = char_limit - 1
        while current_index < (adjusted_char_limit / 2):
            first_string += original_string[current_index]
            second_string = original_string[-current_index - 1] + second_string
            current_index += 1
        first_string += original_string[current_index]
    output = first_string + "..." + second_string
    return output


print(shorten_string("What a beautiful day in the neighborhood", 12))
print(shorten_string("What a beautiful day in the neighborhood", 11))
print(shorten_string("What a beautiful day in the neighborhood", 100))
print(shorten_string("Happy days yours and mine", 8))
