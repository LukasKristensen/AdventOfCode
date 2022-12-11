import copy, math

data = open('day11_data.txt').read().splitlines()
monkey_count, product = 0, 0
monkeys, monkeys_second = [], []


class Monkey:
    def __init__(self, inventory: [], operation_type, operation_number, testing_variables, worried):
        self.inventory = inventory
        self.operation_type = operation_type
        self.operation_number = operation_number
        self.testing_variables = testing_variables
        self.worried = worried
    inspections = 0

    def throw(self):
        self.inspections += 1
        item = self.inventory.pop(0)

        if self.operation_type == 'multiply':
            item *= int(self.operation_number) if self.operation_number != 'old' else item
        if self.operation_type == 'addition':
            item += int(self.operation_number)
        item = int((item/3)-((item/3) % 1)) if self.worried else item % product
        monkeys[self.testing_variables[1]].inventory.append(item) if item % self.testing_variables[0] == 0 else monkeys[self.testing_variables[2]].inventory.append(item)


def calculate_monkey_business(monkeys_input):
    inspections = []
    for monkey in range(len(monkeys_input)):
        inspections.append(monkeys_input[monkey].inspections)
    inspections.sort()
    return inspections[-1]*inspections[-2]


for i in range(int(len(data)/7)+1):
    items_get = list(map(int, data[i*7+1].split(": ")[1].split(", ")))
    operation_type_get = "multiply" if "*" in data[i*7+2] else "addition"
    operation_number_get = data[i*7+2].split(" ")[-1]
    testing_variables_get = [int(data[i*7+3].split(" ")[-1]), int(data[i*7+4].split(" ")[-1]), int(data[i*7+5].split(" ")[-1])]
    new_monkey = Monkey(items_get, operation_type_get, operation_number_get, testing_variables_get, True)
    monkeys.append(new_monkey)
    monkeys_second.append(new_monkey)

    if data == "":
        monkey_count += 1

monkeys_second = copy.deepcopy(monkeys)

for x in range(20):
    for m in monkeys:
        for i in range(len(m.inventory)):
            m.throw()

print("11a:)",calculate_monkey_business(monkeys))


monkeys = monkeys_second
product = math.prod(m.testing_variables[0] for m in monkeys_second)
for m in monkeys:
    m.worried = False

for x in range(10000):
    for m in monkeys:
        for i in range(len(m.inventory)):
            m.throw()

print("11b:)",calculate_monkey_business(monkeys))


