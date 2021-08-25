"""
Reverse a string

For example: input: "cool" output: "looc"
"""

def reverse_string(string):
    ret = ""
    for letter in string:
        ret = letter + ret
    return ret

print(reverse_string("apple"))
