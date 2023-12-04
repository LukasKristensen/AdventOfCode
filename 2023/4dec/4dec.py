data_load = open("input.txt", "r").read().splitlines()
part_one = 0
scratch_cards = {}

for i in range(len(data_load)):
    scratch_cards[i] = 1

for i, val in enumerate(data_load):
    winning_nums = [int(x) for x in filter(None, val.split('|')[0].split(": ")[-1].split(" "))]
    picked_nums = [int(y) for y in filter(None, val.split('|')[1].split(" "))]

    amount_matches = 0
    match_score = 0

    for x in picked_nums:
        if x in winning_nums:
            amount_matches += 1
            if match_score == 0:
                match_score = 1
            else:
                match_score *= 2
    part_one += match_score

    for b in range(1, amount_matches+1):
        scratch_cards[i+b] += scratch_cards[i]

print("Part one:", part_one)
print("Part two:", sum([scratch_cards[b] for b in scratch_cards]))

