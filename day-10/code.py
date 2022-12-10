from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
    "-i", "-input", default="input.txt", dest="file"
)

args = parser.parse_args()

with open(args.file, "r") as file:
    lines = file.read().split('\n')

ADD_INSTRUCTION = "addx"

# PART 1
delta_x = 0
register = 1
total_signal_strength = 0
instruction_idx = 0
cycle = 1
while instruction_idx < len(lines) - 1:
    if (cycle - 20) % 40 == 0:
        total_signal_strength += cycle * register
    if delta_x != 0:
        register += delta_x
        delta_x = 0
    else:
        line = lines[instruction_idx].split(" ")
        if line[0] == ADD_INSTRUCTION:
            delta_x = int(line[1])
        instruction_idx += 1
    cycle += 1
print("PART 1: ", total_signal_strength)

# PART 2
delta_x = 0
CRT_image = ""
register = 1
instruction_idx = 0
cycle = 1
while instruction_idx < len(lines) - 1:
    CRT_image += "#" if register - 1 <= cycle%40 - 1 <= register + 1 else " "
    if delta_x != 0:
        register += delta_x
        delta_x = 0
    else:
        line = lines[instruction_idx].split(" ")
        if line[0] == ADD_INSTRUCTION:
            delta_x = int(line[1])
        instruction_idx += 1
    if cycle %40 == 0:
        CRT_image += "\n"
    cycle += 1
print("PART 2:\n" + CRT_image)
