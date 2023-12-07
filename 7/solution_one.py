import re
import copy
from collections import defaultdict

card_ranks = "AKQJT98765432"

five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pair = []
one_pair = []
high_card = []

hands = []

with open("input.txt") as f:
    for line in f:
        hand = re.search(r"(\w{5}) (\d{1,3})", line)
        hands.append((hand.group(1), int(hand.group(2))))


for hand in hands:
    cards = defaultdict(int)
    for card in hand[0]:
        idx = card_ranks.index(card)
        print(idx)
        cards[card] += 1

    values = sorted(cards.values())
    fives, fours, threes, twos = 0, 0, 0, 0
    for v in values:
        if v == 5:
            fives += 1
        elif v == 4:
            fours += 1
        elif v == 3:
            threes += 1
        elif v == 2:
            twos += 1

    appended_to = ''
    if fives == 1:
        five_of_a_kind.append(hand)
        appended_to = 'five_of_a_kind'
    elif fours == 1:
        four_of_a_kind.append(hand)
        appended_to = 'four_of_a_kind'
    elif threes == 1 and twos == 1:
        full_house.append(hand)
        appended_to = 'full_house'
    elif threes == 1:
        three_of_a_kind.append(hand)
        appended_to = 'three_of_a_kind'
    elif twos == 2:
        two_pair.append(hand)
        appended_to = 'two_pair'
    elif twos == 1:
        one_pair.append(hand)
        appended_to = 'one_pair'
    else:
        high_card.append(hand)
        appended_to = 'high_card'


def sort_hand(hands):
    return sorted(hands, key=lambda hand: [card_ranks.index(c) for c in hand[0]])


def find_strongest(a, b):
    i = 0
    while i < len(a):
        if card_ranks.index(a[0][i]) > card_ranks.index(b[0][i]):
            return b
        elif card_ranks.index(a[0][i]) < card_ranks.index(b[0][i]):
            return a
        i += 1
    return a


def remove_strongest(hands):
    strongest = hands[0]
    for hand in hands:
        strongest = find_strongest(strongest, hand)
    hands.remove(strongest)
    return strongest, hands


# five_of_a_kind = sort_hand(five_of_a_kind)
# four_of_a_kind = sort_hand(four_of_a_kind)
# full_house = sort_hand(full_house)
# three_of_a_kind = sort_hand(three_of_a_kind)
# two_pair = sort_hand(two_pair)
# one_pair = sort_hand(one_pair)
high_card = sort_hand(high_card)
print(high_card)

# ranked_hands = []
# ranked_hands.extend(five_of_a_kind)
# ranked_hands.extend(four_of_a_kind)
# ranked_hands.extend(full_house)
# ranked_hands.extend(three_of_a_kind)
# ranked_hands.extend(two_pair)
# ranked_hands.extend(one_pair)
# ranked_hands.extend(high_card)


total = 0
total_hands = len(hands)

for hand in five_of_a_kind:
    while len(five_of_a_kind) > 0:
        strongest, five_of_a_kind = remove_strongest(five_of_a_kind)
        total += strongest[1] * total_hands
        total_hands -= 1

for hand in four_of_a_kind:
    while len(four_of_a_kind) > 0:
        strongest, four_of_a_kind = remove_strongest(four_of_a_kind)
        total += strongest[1] * total_hands
        total_hands -= 1

for hand in full_house:
    while len(full_house) > 0:
        strongest, full_house = remove_strongest(full_house)
        total += strongest[1] * total_hands
        total_hands -= 1

for hand in three_of_a_kind:
    while len(three_of_a_kind) > 0:
        strongest, three_of_a_kind = remove_strongest(three_of_a_kind)
        total += strongest[1] * total_hands
        total_hands -= 1

for hand in two_pair:
    while len(two_pair) > 0:
        strongest, two_pair = remove_strongest(two_pair)
        total += strongest[1] * total_hands
        total_hands -= 1

for hand in one_pair:
    while len(one_pair) > 0:
        strongest, one_pair = remove_strongest(one_pair)
        total += strongest[1] * total_hands
        total_hands -= 1

for hand in high_card:
    while len(high_card) > 0:
        strongest, high_card = remove_strongest(high_card)
        print(strongest)
        total += strongest[1] * total_hands
        total_hands -= 1

print(total_hands)
print(total)
