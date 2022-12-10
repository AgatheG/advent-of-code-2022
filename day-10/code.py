from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
    "-i", "-input", default="input.txt", dest="file"
)

args = parser.parse_args()

with open(args.file, "r") as file:
    lines = file.read().split('\n')

to_add = 0
X = 1
s = 0
wait = False
idx = 0
cycle = 1
L = [20, 60, 100, 140, 180, 220]
while idx < len(lines) - 1:
    if cycle in L:
        s += cycle * X
    if not wait:
        line = lines[idx].split(" ")
        if line[0] == "addx":
            to_add = int(line[1])
            wait = True
        idx += 1
    else:
        X += to_add
        wait = False
    cycle += 1
print(s)

to_add = 0
s = ""
X = 1
wait = False
idx = 0
cycle = 1
t = False
L = [40 * (i+1) for i in range(5)]
while idx < len(lines) - 1:
    if X - 1 <= cycle%40 - 1 <= X + 1:
        s += "#"
    else:
        s += " "
    if not wait:
        line = lines[idx].split(" ")
        if line[0] == "addx":
            to_add = int(line[1])
            wait = True
        idx += 1
    else:
        X += to_add
        wait = False
    if cycle in L:
        s += "\n"
    cycle += 1
print(s)
