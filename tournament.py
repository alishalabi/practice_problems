"""
Introduction
Tally the results of a small football competition.

Based on an input file containing which team played against which and what the outcome was, create a file with a table like this:

Team                           | MP |  W |  D |  L |  P
Devastating Donkeys            |  3 |  2 |  1 |  0 |  7
Allegoric Alaskans             |  3 |  2 |  0 |  1 |  6
Blithering Badgers             |  3 |  1 |  0 |  2 |  3
Courageous Californians        |  3 |  0 |  1 |  2 |  1
What do those abbreviations mean?

MP: Matches Played
W: Matches Won
D: Matches Drawn (Tied)
L: Matches Lost
P: Points
A win earns a team 3 points. A draw earns 1. A loss earns 0.

The outcome should be ordered by points, descending. In case of a tie, teams are ordered alphabetically.

Input

Your tallying program will receive input that looks like:

Allegoric Alaskans;Blithering Badgers;win
Devastating Donkeys;Courageous Californians;draw
Devastating Donkeys;Allegoric Alaskans;win
Courageous Californians;Blithering Badgers;loss
Blithering Badgers;Devastating Donkeys;loss
Allegoric Alaskans;Courageous Californians;win
The result of the match refers to the first team listed. So this line

Allegoric Alaskans;Blithering Badgers;win
Means that the Allegoric Alaskans beat the Blithering Badgers.

This line:

Courageous Californians;Blithering Badgers;loss
Means that the Blithering Badgers beat the Courageous Californians.

And this line:

Devastating Donkeys;Courageous Californians;draw
Means that the Devastating Donkeys and Courageous Californians tied.

"""

sample1 = ["Allegoric Alaskans", "Blithering Badgers", "win"]
sample2 = ["Devastating Donkeys", "Courageous Californians", "draw"]
sample3 = ["Devastating Donkeys", "Allegoric Alaskans", "win"]
sample4 = ["Courageous Californians", "Blithering Badgers", "loss"]
sample5 = ["Blithering Badgers", "Devastating Donkeys", "loss"]
sample6 = ["Allegoric Alaskans", "Courageous Californians", "win"]

from pprint import pprint


class Tournament:
    def __init__(self):
        self.all_teams = {}

    def input_score(self, score):
        if score[0] not in self.all_teams.keys():
            self.all_teams[score[0]] = {"wins": 0, "match played": 0,
                                        "loses": 0, "draws": 0, "points": 0}
        if score[1] not in self.all_teams.keys():
            self.all_teams[score[1]] = {"wins": 0, "match played": 0,
                                        "loses": 0, "draws": 0, "points": 0}
        if score[2] == "win":
            self.all_teams[score[0]]["wins"] += 1
            self.all_teams[score[0]]["match played"] += 1
            self.all_teams[score[0]]["points"] += 3
            self.all_teams[score[1]]["loses"] += 1
            self.all_teams[score[1]]["match played"] += 1
        if score[2] == "loss":
            self.all_teams[score[1]]["wins"] += 1
            self.all_teams[score[1]]["points"] += 3
            self.all_teams[score[1]]["match played"] += 1
            self.all_teams[score[0]]["loses"] += 1
            self.all_teams[score[0]]["match played"] += 1
        if score[2] == "draw":
            self.all_teams[score[0]]["draws"] += 1
            self.all_teams[score[0]]["points"] += 1
            self.all_teams[score[0]]["match played"] += 1
            self.all_teams[score[1]]["draws"] += 1
            self.all_teams[score[1]]["points"] += 1
            self.all_teams[score[1]]["match played"] += 1
        return self.all_teams

    # TODO: Shoutout to https://github.com/jshams for help with sorting
    def rank_teams(self):
        ret = []
        sorted_teams = sorted(
            self.all_teams, key=lambda x: self.all_teams[x]["points"], reverse=True)
        for item in sorted_teams:
            ret.append([item, self.all_teams[item]["points"], self.all_teams[item]["wins"],
                        self.all_teams[item]["loses"], self.all_teams[item]["draws"], self.all_teams[item]["match played"]])
        pprint(ret)
        return ret


tournament = Tournament()
tournament.input_score(sample1)
tournament.input_score(sample2)
tournament.input_score(sample3)
tournament.input_score(sample4)
tournament.input_score(sample5)
tournament.input_score(sample6)
tournament.rank_teams()
