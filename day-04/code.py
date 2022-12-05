from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
    "-i", "-input", default="input.txt", dest="file")

args = parser.parse_args()

with open(args.file, "r") as file:
    pairs = file.read().split("\n")
    pairs = [p.split(",") for p in pairs]

nb_contained = 0
DELIMITER = "-"
for pair in pairs:
    first_assignement, second_assignment = [p.split(DELIMITER) for p in pair]
    first_lower, first_upper, second_lower, second_upper = [
        int(first_assignement[0]), int(first_assignement[1]),
        int(second_assignment[0]), int(second_assignment[1])
    ]
    if (first_lower <= second_lower and first_upper >= second_upper or
        second_lower <= first_lower and second_upper >= first_upper):
        nb_contained += 1
print("Part 1", nb_contained)

nb_duplicates = 0
for pair in pairs:
    first_assignement, second_assignment = [p.split(DELIMITER) for p in pair]
    first_lower, first_upper, second_lower, second_upper = [
        int(first_assignement[0]), int(first_assignement[1]),
        int(second_assignment[0]), int(second_assignment[1])
    ]
    if (first_lower <= second_lower <= first_upper or first_lower <= second_upper <= first_upper
        or second_lower <= first_lower <= second_upper or second_lower <= first_upper <= second_upper):
        nb_duplicates += 1
print("Part 2", nb_duplicates)
