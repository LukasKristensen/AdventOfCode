data_load = open("input.txt", "r").read().splitlines()
part_one = 0
kickers = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7, '8': 6, '7': 5, '6': 4, '5': 3, '4': 2, '3': 1, '2': 0}
hands = []

for i, val in enumerate(data_load):
    cards, bidding = val.split(" ")

    cards_dict = {}
    for x in cards:
        if x not in cards_dict:
            cards_dict[x] = 1
        else:
            cards_dict[x] += 1

    rank = None
    rank_two = None
    for card, num in enumerate(cards_dict):
        if cards_dict[num] == 5 and not rank:
            rank = 6
    for card, num in enumerate(cards_dict):
        if cards_dict[num] == 4 and not rank:
            rank = 5
    full_house_a, full_house_b = False, False
    for card, num in enumerate(cards_dict):
        if cards_dict[num] == 3:
            full_house_a = True
        if cards_dict[num] == 2:
            full_house_b = True
    if full_house_a and full_house_b and not rank:
        rank = 4
    for card, num in enumerate(cards_dict):
        if cards_dict[num] == 3 and not rank:
            rank = 3
    pair_a, pair_b = False, False
    for card, num in enumerate(cards_dict):
        if not pair_a and cards_dict[num] == 2:
            pair_a = True
        elif cards_dict[num] == 2:
            pair_b = True
    if pair_a and pair_b and not rank:
        rank = 2
    for card, num in enumerate(cards_dict):
        if cards_dict[num] == 2 and not rank:
            rank = 1
    if not rank:
        rank = 0

    kicker_hand = [rank]
    for i in cards:
        kicker_hand.append(kickers[i])
    hands.append([kicker_hand, bidding, cards])


for g in range(len(hands)):
    for x in range(len(hands)-1):
        for k in range(6):
            if hands[x][0][k] > hands[x+1][0][k]:
                break
            elif hands[x][0][k] < hands[x+1][0][k]:
                first_hold, second_hold = hands[x], hands[x+1]
                hands[x], hands[x+1] = second_hold, first_hold
                break

for i in range(len(hands)):
    betting = int(hands[i][1])
    part_one += (len(hands)-i)*betting
print("part one:", part_one)
