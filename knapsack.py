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
# TODO: This algorithm is optimized for "best value", explore how to minimize remaining bag size

sample_items = [(5, 10), (4, 40), (6, 30), (4, 50)]

edge_case1 = [(1, 5), (10, 10), (1, 4)]  # max = 10


def convert_items(item_list):
    unsorted_list = []
    for item in item_list:
        converted_value = item[1] / item[0]
        converted_item = {"ratio": converted_value,
                          "weight": item[0], "value": item[1]}
        unsorted_list.append(converted_item)

    ret = sorted(
        unsorted_list, key=lambda x: x["ratio"], reverse=True)
    return ret


def fill_knapsack(max_weight, item_list):
    sorted_list = convert_items(item_list)
    stolen_items = []  # Not mandatory, but useful if want to return all items, not just value
    remaining_weight = max_weight
    max_value = 0
    for item in sorted_list:
        if item["weight"] < remaining_weight:
            stolen_items.append(item)
            max_value += item["value"]
            remaining_weight -= item["weight"]
    # Idea: check to see is max_value != 0?
    print(f"Max value is {max_value}")
    return max_value


# print(convert_items(sample_items))
fill_knapsack(10, sample_items)
fill_knapsack(10, edge_case1)  # TODO
