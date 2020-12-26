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

hand5 = {
    (2, "clubs"),
    (2, "diamonds"),
    (2, "spades"),
    (3, "clubs"),
    (4, "clubs"),
}

hand6 = {
    (2, "clubs"),
    (2, "diamonds"),
    (3, "spades"),
    (3, "clubs"),
    (4, "clubs"),
}

hand7 = {
    (2, "clubs"),
    (2, "diamonds"),
    (10, "spades"),
    (3, "clubs"),
    (4, "clubs"),
}

hand8 = {
    (2, "clubs"),
    (7, "diamonds"),
    (10, "spades"),
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


def check_pair(values):
    if 2 not in values.values():
        return False
    return True


def check_full_house(values):
    if check_three_of_a_kind(values) == False:
        return False
    if check_pair(values) == False:
        return False
    return True


def check_two_pairs(values):
    count = 0
    for key in values:
        if values[key] == 2:
            count += 1
    if count != 2:
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
    if check_three_of_a_kind(values):
        return ("three of a kind", 4)
    if check_two_pairs(values):
        return ("two pairs", 5)
    if check_pair(values):
        return ("pair", 6)
    return ("high card", 7)


def compare_hands(hands_array):
    high_hand = None
    for hand in hands_array:
        converted_hand = score_one_hand(hand)
        if high_hand == None:
            high_hand = converted_hand
        if converted_hand[1] < high_hand[1]:
            high_hand = hand
    return high_hand[0]

# Tests: one hand
# print(score_one_hand(hand1))
# print(score_one_hand(hand2))
# print(score_one_hand(hand3))
# print(score_one_hand(hand4))
# print(score_one_hand(hand5))
# print(score_one_hand(hand6))
# print(score_one_hand(hand7))
# print(score_one_hand(hand8))


# Tests: compare hands
compare1 = [hand1, hand4, hand5]
compare2 = [hand2, hand4, hand5]
compare3 = [hand6, hand7, hand8]
print(compare_hands(compare1))
print(compare_hands(compare2))
print(compare_hands(compare3))
