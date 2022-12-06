from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
    "-i", "-input", default="input.txt", dest="file"
)
parser.add_argument(
    "-s", "-size", default="4", type=int, dest="marker_size"
)

args = parser.parse_args()

with open(args.file, "r") as file:
    line = file.read()

MARKER_SIZE = args.marker_size
offset = 0
while True:
    potential_marker = line[offset : offset + MARKER_SIZE]
    if len(set(potential_marker)) == MARKER_SIZE:
        break
    offset += 1
print(offset + MARKER_SIZE)