import re
from collections import defaultdict

hands = []
alphabet = "AKQJT98765432"
FIVE = 7
FOUR = 6
FULL = 5
THREE = 4
TWO = 3
ONE = 2
HIGH = 1

with open("sample.txt") as f:
    for line in f:
        hand = re.search(r"(\w{5}) (\d{1,3})", line)
        hands.append([hand.group(1), int(hand.group(2))])

hands_with_type = []
for hand in hands:
    cards = defaultdict(int)
    for card in hand[0]:
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
        hand.append(FIVE)
        hands_with_type.append(hand)
        appended_to = 'five_of_a_kind'
    elif fours == 1:
        hand.append(FOUR)
        hands_with_type.append(hand)
        appended_to = 'four_of_a_kind'
    elif threes == 1 and twos == 1:
        hand.append(FULL)
        hands_with_type.append(hand)
        appended_to = 'full_house'
    elif threes == 1:
        hand.append(THREE)
        hands_with_type.append(hand)
    elif twos == 2:
        hand.append(TWO)
        hands_with_type.append(hand)
    elif twos == 1:
        hand.append(ONE)
        hands_with_type.append(hand)
    else:
        hand.append(HIGH)
        hands_with_type.append(hand)

hands_with_type = sorted(hands_with_type, key=lambda x: x[2], reverse=True)
print(hands_with_type)


def get_strongest(hands):
    strongest = hands[0]
    for hand in hands[1:]:
        if hand[2] == strongest[2]:
            i = 0
            strongest_cards = strongest[0]
            hand_cards = hand[0]
            while i < len(strongest_cards):
                if alphabet.index(strongest_cards[i]) < alphabet.index(hand_cards[i]):
                    break
                elif alphabet.index(strongest_cards[i]) > alphabet.index(hand_cards[i]):
                    strongest = hand
                    break
                i += 1

        else:
            break

    hands.remove(strongest)
    return strongest, hands


total = 0
total_hands = len(hands_with_type)
while len(hands_with_type) > 0:
    strongest, hands_with_type = get_strongest(hands_with_type)
    total += strongest[1] * total_hands
    total_hands -= 1
    print(strongest, total)

print(total)
