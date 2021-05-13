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
        current_Node = self.root
        for letter in prefix:
            if letter not in current_Node.children:
                return []
            current_Node = current_Node.children[letter]
        return self._DFS(current_Node, prefix)

    def _DFS(self, node, prefix):
        words = []
        if node.isWord:
            words.append(prefix)
        for letter in node.children:
            words.append(self._DFS(node.children[letter], prefix + letter))
        return words


test_tree = PrefixTree()
test_tree.insert("cat")
test_tree.insert("catdog")
test_tree.insert("cats")
test_tree.insert("dogs")
test_tree.insert("door")
test_tree.insert("doll")
# print(test_tree.search("cat"))
# print(test_tree.search("dog"))
print(test_tree.starts_with("do"))
print(test_tree.starts_with("ca"))
