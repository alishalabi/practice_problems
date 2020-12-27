"""
Introduction
Given a string containing brackets [], braces {}, parentheses (), or any
combination thereof, verify that any and all pairs are matched and nested correctly.
"""

sample1 = "()][Apple"
sample2 = "[(Happy Days{})]"
sample3 = "[((([[[{{(Happy Days{})}}]]])))]"

brackets = {
    "[": "]",
    "{": "}",
    "(": ")"
}


def sanitize(string):
    ret = []
    for letter in string:
        if letter in brackets.keys() or letter in brackets.values():
            ret.append(letter)
    return ret


def is_valid(string):
    sanitized = sanitize(string)
    # Early exit: odd number of brackets
    if len(sanitized) % 2 != 0:
        return False
    while len(sanitized) > 0:
        if sanitized[-1] != brackets[sanitized[0]]:
            return False
        else:
            sanitized = sanitized[1:-1]
    return True


# print(sanitize(sample1))
# print(sanitize(sample2))
print(is_valid(sample1))
print(is_valid(sample2))
print(is_valid(sample3))
