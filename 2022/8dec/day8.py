data = open('day8_validation.txt').read().splitlines()
trees_visible = 0

for y in range(1, len(data) - 1):

    for x in range(1, len(data[0])-1):
        up_visible = True
        down_visible = True
        left_visible = True
        right_visible = True

        for up in range(1, y+1):
            if data[x][y-up-1] >= data[x][y]:
                up_visible = False
                break
        for down in range(y, len(data)-y-1):
            if data[x][y+down] >= data[x][y]:
                down_visible = False
                break
        for left in range(1, x+1):
            print("[LEFT]","X:", x, "Y:", y, "Val:", data[x][y],"Checking left:",data[x-left][y],"Left:",left)
            if data[x-left][y] >= data[x][y]:
                left_visible = False
                break
        for right in range(x, len(data[0])-x-1):
            if data[x+right][y] >= data[x][y]:
                right_visible = False
                break
        print("X:",x,"Y:",y,"Val:",data[x][y],up_visible,down_visible,left_visible,right_visible)
        if up_visible or down_visible or left_visible or right_visible:
            trees_visible+=1

print("Summed visible:",trees_visible)

# 7855 too high