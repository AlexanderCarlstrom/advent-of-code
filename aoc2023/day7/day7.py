from collections import Counter, defaultdict
from functools import cmp_to_key
import utils

CARDS_1 = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
CARDS_2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


def rank_cards(cards, part):
    char_set = Counter(cards)

    if part == 2:
        j_count = char_set.pop('J', 0)
        if not char_set:
            return 7

        sorted_dict = sorted(char_set.items(), key=lambda x: x[1], reverse=True)
        card, count = sorted_dict[0]
        sorted_dict[0] = (card, count + j_count)
        char_set = dict(sorted_dict)

    if 5 in char_set.values():
        return 7
    if 4 in char_set.values():
        return 6
    if {3, 2}.issubset(set(char_set.values())):
        return 5
    if 3 in char_set.values():
        return 4
    if Counter(char_set.values())[2] == 2:
        return 3
    if 2 in char_set.values():
        return 2
    return 1


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid


def compare_cards(hand1, hand2, part=1):
    diff = rank_cards(hand1.cards, part) - rank_cards(hand2.cards, part)
    if part == 1:
        CARDS = CARDS_1
    else:
        CARDS = CARDS_2

    if diff != 0:
        return diff
    else:
        for i in range(0, len(hand1.cards)):
            diff = CARDS.index(hand1.cards[i]) - CARDS.index(hand2.cards[i])

            if diff != 0:
                return -diff


def solve_p1():
    data = utils.parse_multiple_string('in.txt')
    hands = [Hand(d[0], int(d[1])) for d in data]
    hands = sorted(hands, key=cmp_to_key(compare_cards))

    return sum(i * c.bid for i, c in enumerate(hands, 1))


def solve_p2():
    data = utils.parse_multiple_string('in.txt')
    hands = [Hand(d[0], int(d[1])) for d in data]
    hands = sorted(hands, key=cmp_to_key(lambda a, b: compare_cards(a, b, 2)))

    return sum(i * c.bid for i, c in enumerate(hands, 1))


print('Part 1:', solve_p1())
print('Part 2:', solve_p2())

