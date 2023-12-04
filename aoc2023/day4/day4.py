from collections import defaultdict

import utils
import re

D = utils.parse_single_string('in.txt')
points = 0
cards = []

for card in D:
    pattern = re.compile(r'Card +\d+: ([^|]*) \| ([^|]*)')
    groups = pattern.search(card).groups()
    winning, given = [set(int(n.strip()) for n in num.split()) for num in groups]

    winning.intersection_update(given)
    cards.append([len(winning), 1])
    if len(winning) > 0:
        p = 1
        for w in range(len(winning) - 1):
            p = p * 2
        points += p

for i, card in enumerate(cards):
    for j in range(i + 1, i + card[0] + 1):
        cards[j][1] += card[1]

sum_cards = 0
for card in cards:
    sum_cards += card[1]

print('Part 1:', points)
print('Part 2:', sum_cards)
