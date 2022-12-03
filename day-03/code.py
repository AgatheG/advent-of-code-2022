from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
    "-i", "-input", default="input.txt", dest="file")

args = parser.parse_args()

with open(args.file, "r") as file:
    sacks = file.read().split("\n")

def get_priority(item):
    unicode = ord(item)
    if unicode >= ord("a"):
        return unicode - ord("a") + 1
    return unicode - ord("A") + 27

s = 0
for sack in sacks:
    idx = int(len(sack)/2)
    first_container, second_container = set(sack[:idx]), set(sack[idx:])
    common_item = first_container & second_container
    s += get_priority(common_item.pop())
print(s)

s = 0
for i in range(int(len(sacks)/3)):
    first_sack, second_sack, third_sack = sacks[i*3:i*3+3]
    common_item = set(first_sack) & set(second_sack) & set(third_sack)
    s += get_priority(common_item.pop())
print(s)
