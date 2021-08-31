"""
A burger restaurant wants to be the first to offer 1,000,000 possible combinations of
toppings.
How many menu items will they need?
"""

import combinations

target = 1000000

def how_many_combinations(target):
    arr = []
    combos = combinations.all_combinations(arr)
    counter = 1
    while len(combos) < target:
        arr.append(counter)
        counter += 1
        combos = combinations.all_combinations(arr)
    return len(arr)

print(how_many_combinations(target))
