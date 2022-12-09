H, T = [0,0], [0,0]
T_visit = {}

for i in open('day9_data.txt').read().splitlines():
    direction, distance = i.split(" ")
    for x in range(int(distance)):
        previous_head = H.copy()
        if direction == 'U':
            H[1] += 1
        elif direction == 'D':
            H[1] -= 1
        elif direction == 'R':
            H[0] += 1
        elif direction == 'L':
            H[0] -= 1
        for d in range(2):
            if abs(H[d]-T[d]) > 1:
                T = previous_head
                T_visit[str(T[0])+" "+str(T[1])] = 0
                break
print("9a", len(T_visit)+1)

