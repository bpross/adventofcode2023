from collections import defaultdict

card_rank = '23456789TJQKA'

hands = []
five_of_a_kind = []
four_of_a_kind = []
full_house = []
three_of_a_kind = []
two_pairs = []
one_pair = []
high_card = []

with open('input.txt') as f:
    for line in f:
        hands.append(line.strip().split(' '))

for hand in hands:
    counts = defaultdict(int)
    for card in hand[0]:
        counts[card] += 1

    print(counts)

    one, two, three, four, five = 0, 0, 0, 0, 0

    for v in counts.values():
        if v == 1:
            one += 1
        elif v == 2:
            two += 1
        elif v == 3:
            three += 1
        elif v == 4:
            four += 1
        elif v == 5:
            five += 1

    if five == 1:
        five_of_a_kind.append(hand)
    elif four == 1:
        four_of_a_kind.append(hand)
    elif three == 1 and two == 1:
        full_house.append(hand)
    elif three == 1 and two != 1:
        three_of_a_kind.append(hand)
    elif two == 2 and three != 2:
        two_pairs.append(hand)
    elif two == 1:
        one_pair.append(hand)
    else:
        high_card.append(hand)

five_of_a_kind.sort(
    key=lambda hand: [card_rank.index(c) for c in hand[0]])
four_of_a_kind.sort(
    key=lambda hand: [card_rank.index(c) for c in hand[0]])
full_house.sort(key=lambda hand: [card_rank.index(c) for c in hand[0]])
three_of_a_kind.sort(key=lambda hand: [card_rank.index(c) for c in hand[0]])
two_pairs.sort(key=lambda hand: [card_rank.index(c) for c in hand[0]])
one_pair.sort(key=lambda hand: [card_rank.index(c) for c in hand[0]])
high_card.sort(key=lambda hand: [card_rank.index(c) for c in hand[0]])

print('five_of_a_kind', five_of_a_kind)
print('four_of_a_kind', four_of_a_kind)
print('full_house', full_house)
print('three_of_a_kind', three_of_a_kind)
print('two_pairs', two_pairs)
print('one_pair', one_pair)
print('high_card', high_card)


ranked_hands = high_card + one_pair + two_pairs + \
    three_of_a_kind + full_house + four_of_a_kind + five_of_a_kind

total = 0
hand = 1
for h in ranked_hands:
    print(hand, h)
    total += int(h[1]) * hand
    hand += 1

print(total)
