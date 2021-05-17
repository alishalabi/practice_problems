"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example: strs = ["flowers", "flow", "flight"]
output = "fl"

strs = ["dog", "racecar", "car"]
"""

sample1 = ["flowers", "flow", "flight"]
def longest_prefix(array):
    ret = ""
    shortest = min(sample1, key=len)
    for index in range(len(shortest) - 1):
        for word in array:
            if shortest[index] != word[index]:
                return ret
        ret += shortest[index]
    return ret


print(longest_prefix(sample1))
