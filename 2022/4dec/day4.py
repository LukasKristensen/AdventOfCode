score = 0
second_score = 0

for i in open('day4_data.txt').read().splitlines():
    first_range, second_range = i.split(',')
    a, b = map(int, first_range.split('-'))
    c, d = map(int, second_range.split('-'))

    if (a <= c <= d <= b) or (c <= a <= b <= d):
        score += 1

    if a <= d and c <= b:
        second_score += 1

print("4a)", score)
print("4b)", second_score)

