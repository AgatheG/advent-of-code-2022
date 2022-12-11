from argparse import ArgumentParser
from collections import deque
import numpy as np

parser = ArgumentParser()
parser.add_argument(
    "-i", "-input", default="input.txt", dest="file"
)

args = parser.parse_args()

with open(args.file, "r") as file:
    monkey_descs = file.read().split('\n\n')

class Monkey(object):
    def __init__(self, items, string_method, threshold, true_monkey, false_monkey, div):
        self.items = np.array([int(item) for item in items])
        self.operation = eval("lambda old: " + string_method)
        self.divisible_test_threshold = threshold
        self.true_monkey = true_monkey
        self.false_monkey = false_monkey
        self.inspections = 0
        self.div = div

    def get_manageable_worry_level(self):
        if self.div:
            return self.operation(self.items) % self.div
        return (self.operation(self.items) / 3).astype(int)


    def inspect(self, div=None):
        self.inspections += len(self.items)
        worry_levels = self.get_manageable_worry_level()
        assignments = worry_levels % self.divisible_test_threshold
        self.items = np.array([])
        return worry_levels[assignments == 0], worry_levels[assignments != 0]

    def add(self, new_items):
        self.items = np.append(self.items, new_items)

# Parsing
def parse(div=None):
    monkeys = {}
    for desc in monkey_descs:
        desc = desc.split('\n')

        items = desc[1].split(": ")[-1].split(", ")
        operation = desc[2].split(": new = ")[1]
        threshold = int(desc[3].split(" ")[-1])
        true_monkey = int(desc[4].split(" ")[-1])
        false_monkey = int(desc[5].split(" ")[-1])
        monkeys[len(monkeys)] = Monkey(items, operation, threshold, true_monkey, false_monkey, div)
    return monkeys

# PART 1

def monkey_business(monkeys, rounds):
    for i in range(rounds):
        for monkey_idx in range(len(monkeys)):
            monkey = monkeys[monkey_idx]
            true_items, false_items = monkey.inspect()
            monkeys[monkey.true_monkey].add(true_items)
            monkeys[monkey.false_monkey].add(false_items)
    inspections = sorted([monkey.inspections for monkey in monkeys.values()])[-2:]
    return inspections[0] * inspections[1]

MONKEYS = parse()
print(monkey_business(MONKEYS, 20))

# PART 2
full_div = 1
for monkey_idx in range(len(MONKEYS)):
    monkey = MONKEYS[monkey_idx]
    monkey.inspections = 0
    full_div *= monkey.divisible_test_threshold
print(monkey_business(parse(full_div), 10000))
