"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example: strs = ["flowers", "flow", "flight"]
output = "fl"

strs = ["dog", "racecar", "car"]
"""

sample1 = ["flowers", "flow", "flight"]

# Method 1: brute force, nested loops
def longest_prefix(array):
    ret = ""
    shortest = min(sample1, key=len)
    for index in range(len(shortest) - 1):
        for word in array:
            if shortest[index] != word[index]:
                return ret
        ret += shortest[index]
    return ret

# Method 2: prefix tree
class Node:
    def __init__(self, data):
        self.data = None
        self.children = {}

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = Node()
            current.children[letter] = current

    def build(self, words):
        for word in words:
            self.insert(word)

    def longest_prefix(self):
        ret = ""
        current = self.root
        if len(current.children.keys()) == 1:
            ret += current.children.keys()[0]
            current.



print(longest_prefix(sample1))
