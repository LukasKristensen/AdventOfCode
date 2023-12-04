data_load = open("input.txt", "r").read().splitlines()
part_one, part_two = 0, 0
scratch_cards = {}

for i in range(len(data_load)):
    scratch_cards[i] = 1

for i in range(len(data_load)):
    winning_nums, picked_nums = data_load[i].split(' | ')
    winning_nums_sorted = filter(None, winning_nums.split(": ")[-1].replace("  ", " ").split(" "))
    picked_nums_sorted = filter(None, picked_nums[0:].replace("  ", " ").split(" "))

    new_winning = [int(x) for x in winning_nums_sorted]
    new_picked = [int(y) for y in picked_nums_sorted]

    amount_matches = 0
    match_score = 0

    for x in new_picked:
        if x in new_winning:
            amount_matches += 1
            if match_score == 0:
                match_score = 1
            else:
                match_score *= 2
    part_one += match_score

    for b in range(1, amount_matches+1):
        scratch_cards[i+b] += 1*scratch_cards[i]

print("Part one:", part_one)
print("Part two:", sum([scratch_cards[b] for b in scratch_cards]))

