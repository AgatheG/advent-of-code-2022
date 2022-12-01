from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
    "-i", "-input", default="input.txt", dest="file")

args = parser.parse_args()

with open(args.file, "r") as file:
    raw_calories = file.read().split("\n\n")
    calories = [
        sum(int(item_calory) for item_calory in calories_per_elf.split("\n"))
        for calories_per_elf in raw_calories
    ]

# PART 1
print(max(calories))

# PART 2
print(sum(sorted(calories)[-3:]))
