print("1a)",sum([1 if i == "(" else -1 for i in open('day1_data.txt').read().splitlines()[0]]))

