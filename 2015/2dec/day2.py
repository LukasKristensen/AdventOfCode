paper_wrap, ribbon = 0, 0
for i in open('day2_data.txt').read().splitlines():
    l, w, h = map(int, i.split("x"))
    paper_wrap += 2*l*w+2*w*h+2*h*l+min([l*w,l*h,w*h])
    ribbon += 2*sorted([l, w, h])[1]+2*sorted([l, w, h])[0]+w*l*h
print("2a)",paper_wrap)
print("2b)",ribbon)

