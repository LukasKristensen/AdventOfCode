data = open('day11_data.txt').read().splitlines()
monkey_count = 0
monkeys = []


def print_invenstories():
    print("PRINTING INVENTORIES:......")
    for m in monkeys:
        print(m.inventory)


class Monkey:
    def __init__(self, inventory: [], operation_type, operation_number, testing_variables):
        self.inventory = inventory
        self.operation_type = operation_type
        self.operation_number = operation_number
        self.testing_variables = testing_variables
    inspections = 0

    def throw(self):
        self.inspections += 1
        item = self.inventory.pop(0)
        print("Inspection item:",item)

        if self.operation_type == 'multiply':
            if self.operation_number != 'old':
                print("-Multipying",item,"With:",self.operation_number)
                item *= int(self.operation_number)
            else:
                print("-Multipying",item,"With:",item)
                item *= item
        if self.operation_type == 'addition':
            print("-Adding", item, "With:", self.operation_number)
            item += int(self.operation_number)

        item = (item/3)
        print("Item:",item,"Modulo:",(item%1))
        item = int(item-(item%1))
        print("-- Bored:",item)

        # print("Checking if:",item % self.testing_variables[0],"Based:",item,self.testing_variables[0])
        if item % self.testing_variables[0] == 0:
            print("---Throwing:",item,"To:",self.testing_variables[1],"INSTEAD OF:",self.testing_variables[2])
            monkeys[self.testing_variables[1]].inventory.append(item)
        else:
            print("---Throwing:",item,"To:",self.testing_variables[2],"INSTEAD OF:",self.testing_variables[1])
            monkeys[self.testing_variables[2]].inventory.append(item)


for i in range(int(len(data)/7)+1):
    items_get = list(map(int, data[i*7+1].split(": ")[1].split(", ")))
    operation_type_get = "multiply" if "*" in data[i*7+2] else "addition"
    operation_number_get = data[i*7+2].split(" ")[-1]
    testing_variables_get = [int(data[i*7+3].split(" ")[-1]), int(data[i*7+4].split(" ")[-1]), int(data[i*7+5].split(" ")[-1])]
    print("Received variables:",items_get, operation_type_get, operation_number_get, testing_variables_get)
    new_monkey = Monkey(items_get, operation_type_get, operation_number_get, testing_variables_get)
    monkeys.append(new_monkey)

    if data == "":
        monkey_count += 1


for x in range(20):
    print("\nROUND:",x)
    print_invenstories()
    #input()
    for m in monkeys:
        for i in range(len(m.inventory)):
            m.throw()

inspections = []
for m in monkeys:
    inspections.append(m.inspections)
# print("Unsorted:",inspections)
inspections.sort()


print("11a:)",inspections[-1]*inspections[-2])

