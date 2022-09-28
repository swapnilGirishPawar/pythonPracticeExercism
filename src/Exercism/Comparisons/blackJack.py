"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

from re import T


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card == 'K':
        return 10
    elif card == 'J':
        return 10
    elif card == 'Q':
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)
# print("Card = ", value_of_card('Q'))


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if value_of_card(card_one) == value_of_card(card_two):
        return (card_one, card_two)
    elif value_of_card(card_one) < value_of_card(card_two):
        return card_two
    elif value_of_card(card_one) > value_of_card(card_two):
        return card_one
# print(higher_card('9', '9'))


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    if value_of_card(card_one)+value_of_card(card_two) > 10:
        return 1
    elif card_one == 'A' or card_two == 'A':
        return 1
    else:
        return 11
# print(value_of_ace('A', '2'))


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    if (card_one == 'A' and value_of_card(card_two) == 10) or (card_two == 'A' and value_of_card(card_one) == 10):
        return True
    else:
        return False
# print(is_blackjack("A", "A"))


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    return (value_of_card(card_one) == value_of_card(card_two)) or ((card_one == 'Q' and card_two == 'K') or card_one == 'K' and card_two == 'Q')
# print(can_split_pairs('Q', '1'))


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    print(value_of_card(card_one)+value_of_card(card_two))
    val = value_of_card(card_one)+value_of_card(card_two)

    if (11 >= val >= 9):
        return True
    else:
        return False


print(can_double_down('10', 'A'))
