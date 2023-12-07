from collections import Counter, defaultdict

import utils
import re

card_types = {
    '2': 0,
    '3': 1,
    '4': 2,
    '5': 3,
    '6': 4,
    '7': 5,
    '8': 6,
    '9': 7,
    'T': 8,
    'J': 9,
    'Q': 10,
    'K': 11,
    'A': 12
}


def get_card_price(card):
    char_set = Counter(card[0])

    if 5 in char_set.values():
        return 7
    if 4 in char_set.values():
        return 6
    if {3, 2}.issubset(set(char_set.values())):
        return 5
    if 3 in char_set.values():
        return 4
    if {2, 2}.issubset(set(char_set.values())):
        return 3
    if 2 in char_set.values():
        return 2
    if len(char_set) == 5:
        return 1

    return 0


def solve_p1():
    cards = utils.parse_multiple_string('ex.txt')

    n = len(cards)

    for i in range(n):
        for j in range(0, n - i - 1):

            p1 = get_card_price(cards[j])
            p2 = get_card_price(cards[j + 1])

            if p1 > p2:
                cards[j], cards[j + 1] = cards[j + 1], cards[j]
            elif p1 == p2:
                for ii in range(0, len(cards[j])):
                    if card_types[cards[j][ii]] > card_types[cards[j + 1][ii]]:
                        cards[j], cards[j + 1] = cards[j + 1], cards[j]
                        break

    print(cards)


print('Part 1:', solve_p1())