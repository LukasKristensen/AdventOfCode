data_load = open("input.txt", "r").read().splitlines()
part_two = 0
kickers = {'A': 12, 'K': 11, 'Q': 10, 'J': -1, 'T': 8, '9': 7, '8': 6, '7': 5, '6': 4, '5': 3, '4': 2, '3': 1, '2': 0}
hands = []

for i, val in enumerate(data_load):
    cards, bidding = val.split(" ")
    cards_dict = {}
    for x in cards:
        if x not in cards_dict:
            cards_dict[x] = 1
        else:
            cards_dict[x] += 1
    if 'J' not in cards_dict:
        cards_dict['J'] = 0
    rank = None
    for card, num in enumerate(cards_dict):
        if (cards_dict[num] == 5 or (cards_dict[num]+cards_dict['J'] == 5 and num != 'J')) and not rank:
            rank = 6
    for card, num in enumerate(cards_dict):
        if (cards_dict[num] == 4 or (cards_dict[num]+cards_dict['J'] == 4 and num != 'J')) and not rank:
            rank = 5
    full_house = False
    for card, num in enumerate(cards_dict):
        for card2, num2 in enumerate(cards_dict):
            if num == num2:
                pass
            elif cards_dict[num] == 3 and cards_dict[num2] == 2:
                full_house = True
            elif cards_dict[num]+cards_dict['J'] == 3 and cards_dict[num2] == 2 and num2 != 'J':
                full_house = True
            elif cards_dict[num2]+cards_dict['J'] == 3 and cards_dict[num] == 2 and num != 'J':
                full_house = True

    if full_house and not rank:
        rank = 4
    for card, num in enumerate(cards_dict):
        if (cards_dict[num] == 3 or (cards_dict[num]+cards_dict['J'] == 3 and num != 'J')) and not rank:
            rank = 3
    pair = False
    for card, num in enumerate(cards_dict):
        for card2, num2 in enumerate(cards_dict):
            if num == num2:
                continue
            elif cards_dict[num] == 2 and cards_dict[num2] == 2:
                pair = True
            elif cards_dict[num]+cards_dict['J'] == 2 and cards_dict[num2] == 2 and num != 'J':
                pair = True
            elif cards_dict[num] == 2 and cards_dict[num2]+cards_dict['J'] == 2 and num2 != 'J':
                pair = True
    if pair and not rank:
        rank = 2
    for card, num in enumerate(cards_dict):
        if (cards_dict[num] == 2 or (cards_dict[num]+cards_dict['J'] == 2 and num != 'J')) and not rank:
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
    part_two += (len(hands)-i)*betting
print("part two:", part_two)
