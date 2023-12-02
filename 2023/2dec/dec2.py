game_ids_valid = []
set_powers = []
color_constraints = {'red': 12, 'green': 13, 'blue': 14}

for i in open("input.txt", "r").read().splitlines():
    game_id, draws = i.split(": ")
    game_id, draws = int(game_id.split(" ")[-1]), draws.split("; ")
    color_draws = {"red": 0, "green": 0, "blue": 0}
    game_valid = True

    for x in draws:
        values = x.split(", ")
        for val_color in values:
            val, color = val_color.split(" ")
            if color_constraints[color] < int(val):
                game_valid = False
            if color_draws[color] < int(val):
                color_draws[color] = int(val)
    if game_valid:
        game_ids_valid.append(game_id)
    set_powers.append(color_draws['red']*color_draws['green']*color_draws['blue'])

print("Part 1:", sum(game_ids_valid))
print("Part 2:", sum(set_powers))

