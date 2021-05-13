"""
In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.



Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.
Example 2:

Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.
Example 3:

Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).

"""
# Inspired by thecodingworld's youtube channel

words1 = ["hello","leetcode"]
order1 = "hlabcdefgijkmnopqrstuvwxyz"

words2 = ["word","world","row"]
order2 = "worldabcefghijkmnpqstuvxyz"

words3 = ["apple","app"]
order3 = "abcdefghijklmnopqrstuvwxyz"

def is_valid(words, order):
    adjusted_dict = {}
    for index in range(len(order)):
        adjusted_dict[order[index]] = index
    for index in range(len(words) - 1):
        word1 = words[index]
        word2 = words[index + 1]
        for i in range(min(len(word1), len(word2))):
            if word1[i] != word2[i]:
                if adjusted_dict[word1[i]] > adjusted_dict[word2[i]]:

                    return False
                break
            if len(word1) > len(word2):
                return False
    return True



print(is_valid(words1, order1))
print(is_valid(words2, order2))
print(is_valid(words3, order3))
