data = open('day2_data.txt').read().splitlines()
paper_wrap = 0
for i in data:
    l, w, h = map(int, i.split("x"))
    paper_wrap += 2*l*w+2*w*h+2*h*l+min([l*w,l*h,w*h])
print("1a)",paper_wrap)

# 1731664 too high