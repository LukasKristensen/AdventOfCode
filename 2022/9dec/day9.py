import numpy as np


H, knots, T_visit_a, T_visit_b = [], [0]*10, {}, {}

for i in open('day9_data.txt').read().splitlines():
    direction, distance = i.split(" ")
    for x in range(int(distance)):
        previous = knots

        if direction == 'U':
            knots[0] += 1
        elif direction == 'D':
            knots[0] -= 1
        elif direction == 'R':
            knots[0] += 1j
        elif direction == 'L':
            knots[0] -= 1j

        for k in range(1, len(knots)):
            difference = knots[k - 1] - knots[k]
            signed_difference = np.sign(difference.real) + 1j * np.sign(difference.imag)
            if abs(difference) >= 2:
                knots[k] += signed_difference
        T_visit_a[str(knots[1])] = 0
        T_visit_b[str(knots[-1])] = 0

print("9a", len(T_visit_a))
print("9b", len(T_visit_b))



