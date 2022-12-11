import copy
import math

data = open('day11_data.txt').read().splitlines()
monkey_count = 0
monkeys, monkeys_second = [], []
product_modulo = 0


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
            if self.operation_number != 'old':
                item *= int(self.operation_number)
            else:
                item *= item
        if self.operation_type == 'addition':
            item += int(self.operation_number)
        if self.worried:
            item = (item/3)
            item = int(item-(item%1))
        else:
            item %= product_modulo
        if item % self.testing_variables[0] == 0:
            monkeys[self.testing_variables[1]].inventory.append(item)
        else:
            monkeys[self.testing_variables[2]].inventory.append(item)


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

inspections = []
for m in range(len(monkeys)):
    inspections.append(monkeys[m].inspections)
inspections.sort()

print("11a:)",inspections[-1]*inspections[-2])


monkeys = monkeys_second
product_modulo = math.prod(m.testing_variables[0] for m in monkeys_second)
for m in monkeys:
    m.worried = False

for x in range(10000):
    for m in monkeys:
        for i in range(len(m.inventory)):
            m.throw()

inspections_not_worried = []
for m in range(len(monkeys)):
    inspections_not_worried.append(monkeys_second[m].inspections)
inspections_not_worried.sort()

print("11b:)",inspections_not_worried[-1]*inspections_not_worried[-2])


