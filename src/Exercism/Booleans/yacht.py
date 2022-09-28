# Score categories.
# Change the values as you see fit.
from collections import Counter
from functools import partial
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score_yacht(dice):
    if len(set(dice)) == 1:
        return 50
    return 0


def score_n(n, dice):
    return sum(d for d in dice if d == n)


def score_full_house(dice):
    if sorted(Counter(dice).values()) == [2, 3]:
        return sum(dice)
    return 0


def score_four_of_kind(dice):
    number, count = Counter(dice).most_common(1)[0]
    if count >= 4:
        return number * 4
    return 0


def score_little_straight(dice):
    if sorted(dice) == [1, 2, 3, 4, 5]:
        return 30
    return 0


def score_big_straight(dice):
    if sorted(dice) == [2, 3, 4, 5, 6]:
        return 30
    return 0


def score_choice(dice):
    return sum(dice)


SCORE = {
    YACHT: score_yacht,
    ONES: partial(score_n, 1),
    TWOS: partial(score_n, 2),
    THREES: partial(score_n, 3),
    FOURS: partial(score_n, 4),
    FIVES: partial(score_n, 5),
    SIXES: partial(score_n, 6),
    FULL_HOUSE: score_full_house,
    FOUR_OF_A_KIND: score_four_of_kind,
    LITTLE_STRAIGHT: score_little_straight,
    BIG_STRAIGHT: score_big_straight,
    CHOICE: score_choice,
}


def score(dice, category):
    return SCORE[category](dice)
