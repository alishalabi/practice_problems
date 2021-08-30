"""
Practicing recursion using classic combination problem.
Inspired by Matthew M Yound https://www.youtube.com/channel/UCEjCzpiD54d7ox6Rjl2SPTg
"""

input = ["ketchup", "lettuce", "mustard", "pickles", "onions", "cheese"]

def all_combinations(input):
    if len(input) == 0:
        return [[]]

    combinations = []
    for combination in all_combinations(input[1:]):
        combinations += [combination, combination + [input[0]]]

    return combinations

print(all_combinations(input))
