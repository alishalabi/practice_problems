"""
Introduction
In this exercise, let's try to solve a classic problem.

Bob is a thief. After months of careful planning, he finally manages to crack the security systems of a high-class apartment.

In front of him are many items, each with a value (v) and weight (w). Bob, of course, wants to maximize the total value he can get; he would gladly take all of the items if he could. However, to his horror, he realizes that the knapsack he carries with him can only hold so much weight (W).

Given a knapsack with a specific carrying capacity (W), help Bob determine the maximum value he can get from the items in the house. Note that Bob can take only one of each item.

All values given will be strictly positive. Items will be represented as a list of pairs, wi and vi, where the first element wi is the weight of the ith item and vi is the value for that item.

For example:

Items: [ { "weight": 5, "value": 10 }, { "weight": 4, "value": 40 }, { "weight": 6, "value": 30 }, { "weight": 4, "value": 50 } ]

Knapsack Limit: 10

For the above, the first item has weight 5 and value 10, the second item has weight 4 and value 40, and so on.

In this example, Bob should take the second and fourth item to maximize his value, which, in this case, is 90. He cannot get more than 90 as his knapsack has a weight limit of 10.
"""

# Assumption: Sacrificing Memory For Run Time

sample_items = [(5, 10), (4, 40), (6, 30), (4, 50)]


def convert_items(item_list):
    unsorted_list = []
    for item in item_list:
        converted_value = item[1] / item[0]
        converted_item = {"ratio": converted_value,
                          "weight": item[0], "value": item[1]}
        unsorted_list.append(converted_item)
    print(unsorted_list)

    def get_key(item):
        return item[0].ratio
    ret = sorted(unsorted_list, key=get_key, reverse=True)
    print(ret)


convert_items(sample_items)
