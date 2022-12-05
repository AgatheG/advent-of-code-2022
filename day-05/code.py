from argparse import ArgumentParser
from collections import deque
import re

parser = ArgumentParser()
parser.add_argument(
    "-i", "-input", default="input.txt", dest="file")

args = parser.parse_args()

with open(args.file, "r") as file:
    stacks, instructions = file.read().split("\n\n")

# Parse stacks (part 1 & 2)
stacks = stacks.split('\n')
N = int(stacks.pop().rstrip()[-1])
stacks_p_1 = [deque() for i in range(N)]
stacks_p_2 = [deque() for i in range(N)]

for row in stacks:
    row = row.replace("[", "").replace("]", "").split(" ")
    stack_idx, row_idx = 0, 0
    while row_idx < len(row):
        elem = row[row_idx]
        if elem != "":
            stacks_p_1[stack_idx].appendleft(elem)
            stacks_p_2[stack_idx].appendleft(elem)
            row_idx += 1
        else:
            row_idx += 4
        stack_idx += 1

PATTERN = 'move\s(\d*)\sfrom\s(\d*)\sto\s(\d*)'

# Parse instructions (part 1 & 2)
instructions = instructions.split("\n")
for instruction in instructions:
    quantity, origin, destination = re.match(PATTERN, instruction).groups()
    quantity, origin, destination = int(quantity), int(origin) - 1, int(destination) - 1
    moved_crates_p_2 = deque() # keep order of crates for p2
    for i in range(quantity):
        crate_p_1 = stacks_p_1[origin].pop()
        crate_p_2 = stacks_p_2[origin].pop()
        stacks_p_1[destination].append(crate_p_1)
        moved_crates_p_2.appendleft(crate_p_2)
    stacks_p_2[destination].extend(moved_crates_p_2)

print("Part 1", "".join([queue[-1] for queue in stacks_p_1]))
print("Part 2", "".join([queue[-1] for queue in stacks_p_2]))
