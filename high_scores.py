"""
Introduction
Manage a game player's High Score list.

Your task is to build a high-score component of the classic Frogger game, one of the highest selling and addictive games of all time, and a classic of the arcade era. Your task is to write methods that return the highest score from the list, the last added score and the three highest scores.

In this exercise, you're going to use and manipulate lists. Python lists are very versatile, and you'll find yourself using them again and again in problems both simple and complex.
"""

# Assumption: input array of tuples
# Assumption: no tied scores
# Assumption: at least 3 scores

sample_input = [
    (5, "Abby"),
    (4, "Billy"),
    (10, "Catalina"),
    (1, "Dennis"),
    (100, "Ernie"),
    (15, "Frank"),
    (2, "Gene")
]


class Scoresheet:
    def __init__(self, score_input):
        self.score_input = score_input
        # Sorting tuple method inspired by https://www.pythoncentral.io/how-to-sort-a-list-tuple-or-object-with-sorted-in-python/

        def get_key(item):
            return item[0]
        self.sorted_input = sorted(self.score_input, key=get_key, reverse=True)

    # Bonus method: add value
    def add_score(self, new_score):
        self.score_input.append(new_score)

        def get_key(item):
            return item[0]
        self.sorted_input = sorted(self.score_input, key=get_key, reverse=True)

    def get_last_score(self):
        last_score = self.score_input[-1]
        print(f"Last score: {last_score[1]} scored {last_score[0]}")

    def get_top_score(self):
        print(f"Top Score: {self.sorted_input[0][1]} scored {self.sorted_input[0][0]}")
        return self.sorted_input[0]

    def get_top_three_scores(self):
        top_three = self.sorted_input[0:3]
        print(f"Top Score: {top_three[0][1]} scored {top_three[0][0]}")
        print(f"Second Top Score: {top_three[1][1]} scored {top_three[1][0]}")
        print(f"Third Top Score: {top_three[2][1]} scored {top_three[2][0]}")
        return top_three


solution = Scoresheet(sample_input)
solution.get_last_score()
solution.get_top_score()
solution.get_top_three_scores()
