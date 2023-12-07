data_load = open("input.txt", "r").read().splitlines()
part_one = 0
kickers = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7, '8': 6, '7': 5, '6': 4, '5': 3, '4': 2, '3': 1, '2': 0}
hands = []

for val in data_load:
    cards, bidding = val.split(" ")

    cards_dict = {}
    for x in cards:
        cards_dict[x] = cards_dict.get(x, 0) + 1

    rank = None
    for num, count in cards_dict.items():
        if count == 5 and not rank:
            rank = 6
        elif count == 4 and not rank:
            rank = 5
    full_house_a = any(count == 3 for count in cards_dict.values())
    full_house_b = any(count == 2 for count in cards_dict.values())
    if full_house_a and full_house_b and not rank:
        rank = 4
    for count in cards_dict.values():
        if count == 3 and not rank:
            rank = 3
    pair_a = pair_b = False
    for count in cards_dict.values():
        if not pair_a and count == 2:
            pair_a = True
        elif count == 2:
            pair_b = True
    if pair_a and pair_b and not rank:
        rank = 2
    for count in cards_dict.values():
        if count == 2 and not rank:
            rank = 1
    rank = rank if rank else 0

    kicker_hand = [rank] + [kickers[i] for i in cards]
    hands.append([kicker_hand, bidding, cards])

hands.sort(key=lambda x: x[0], reverse=True)

for i, hand in enumerate(hands):
    betting = int(hand[1])
    part_one += (len(hands) - i) * betting

print("part one:", part_one)
