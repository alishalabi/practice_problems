"""
Introduction
Pick the best hand(s) from a list of poker hands.

See wikipedia for an overview of poker hands.
"""

# Assumption: no jokers
# Assumption: face cards do not need to be converted (ie Jack -> 11)
# Assumption: aces always high

score_key = {
    "straight flush": 0,
    "four of a kind": 1,
    "full house": 2,
    "flush": 3,
    "staight": 4,
    "three of a kind": 5,
    "two pair": 6,
    "one pair": 7,
    "high card": 8
}

hand1 = {
    (11, "clubs"),
    (10, "clubs"),
    (9, "clubs"),
    (8, "clubs"),
    (7, "clubs")
}

hand2 = {
    (5, "clubs"),
    (5, "spades"),
    (5, "hearts"),
    (5, "diamonds"),
    (2, "clubs"),
}

hand3 = {
    (5, "clubs"),
    (5, "spades"),
    (5, "hearts"),
    (2, "diamonds"),
    (2, "clubs"),
}

hand4 = {
    (2, "clubs"),
    (7, "clubs"),
    (10, "clubs"),
    (3, "clubs"),
    (4, "clubs"),
}


def check_flush(suits):
    if 5 not in suits.values():
        return False
    else:
        return True


def check_straight(values, high_card):
    for i in range(4):
        next_card = high_card - i - 1
        if values[next_card] != 1:
            return False
    return True


def check_straight_flush(suits, values, high_card):
    if check_flush(suits) == False:
        return False
    if check_straight(values, high_card) == False:
        return False
    return True

# Todo: extract high card of four


def check_four_of_a_kind(values):
    if 4 not in values.values():
        return False
    return True


def check_three_of_a_kind(values):
    if 3 not in values.values():
        return False
    return True


def check_full_house(values):
    if 3 not in values.values():
        return False
    if 2 not in values.values():
        return False
    return True


def score_one_hand(hand):
    suits = {
        "clubs": 0,
        "spades": 0,
        "hearts": 0,
        "diamonds": 0
    }
    values = {
        14: 0,
        13: 0,
        12: 0,
        11: 0,
        10: 0,
        9: 0,
        8: 0,
        7: 0,
        6: 0,
        5: 0,
        4: 0,
        3: 0,
        2: 0,
    }
    high_card = 0
    for card in hand:
        suit = card[1]
        suits[suit] += 1
        value = card[0]
        if value > high_card:
            high_card = value
        values[value] += 1
    if check_straight_flush(suits, values, high_card):
        return ("straight flush", 0)
    if check_four_of_a_kind(values):
        return ("four of a kind", 1)
    if check_full_house(values):
        return ("full house", 2)
    if check_flush(suits):
        return ("flush", 3)


print(score_one_hand(hand1))
print(score_one_hand(hand2))
print(score_one_hand(hand3))
print(score_one_hand(hand4))
