"""
Implement a prefix tree with insert, contains, starts with.
"""

# Inspired by Timothy Chang's Youtube channel

class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False

class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        current_Node = self.root

        for letter in word:
            if letter not in current_Node.children:
                current_Node.children[letter] = Node()
            current_Node = current_Node.children[letter]
        current_Node.isWord = True

    def search(self, word):
        current_Node = self.root
        for letter in word:
            if letter not in current_Node.children:
                return False
            current_Node = current_Node.children[letter]
        if current_Node.isWord == True:
            return True
        else:
            return False

    def starts_with(self, prefix):
        # TODO: depth first search
        # current_Node = self.root
        # for letter in word:
        #     if letter not in current_Node.children:
        #         return False
        #     current_Node = current_Node.children[letter]


test_tree = PrefixTree()
test_tree.insert("cat")
test_tree.insert("catdog")
test_tree.insert("cats")
print(test_tree.search("cat"))
print(test_tree.search("dog"))
