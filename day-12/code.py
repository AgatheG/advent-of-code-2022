from argparse import ArgumentParser
import numpy as np

parser = ArgumentParser()
parser.add_argument(
    "-i", "-input", default="input.txt", dest="file"
)

args = parser.parse_args()

with open(args.file, "r") as file:
    lines = file.read().split('\n')

END = "E"
START = "S"
REAL_END = "z"
REAL_START = "a"

def get_position_elem(condition):
    matches = np.where(condition)
    if len(matches):
        return matches[0][0], matches[1][0]
    return -1, -1

def find_next(distances, not_visited):
    only_not_visited_distances = distances[not_visited]
    if only_not_visited_distances.size:
        current_min_distance = np.min(only_not_visited_distances)
        return get_position_elem(not_visited & (distances == current_min_distance))

def update_neighbors(row, col, distances):
    elem = ELEVATIONS[row, col]
    distance_to_elem = distances[row, col]
    indices = [[row - 1, col], [row + 1, col], [row, col - 1], [row, col + 1]]
    for i, j in indices:
        if i >= 0 and j >= 0 and i < ELEVATIONS.shape[0] - 1 and j < ELEVATIONS.shape[1] - 1:
            next_elem = REAL_END if ELEVATIONS[i, j] == END else ELEVATIONS[i, j]
            distance_to_next = distances[i, j]
            if ord(next_elem) <= 1 + ord(elem):
                distances[i, j] = min(distance_to_elem + 1, distance_to_next)

def path_between_S_E(row, col):
    not_visited = np.ones(ELEVATIONS.shape, dtype="bool")
    distances = np.ones(ELEVATIONS.shape) * float("inf")

    distances[row, col] = 0
    next = [row, col]

    while next:
        row, col = next
        not_visited[row, col] = False
        update_neighbors(row, col, distances)
        next = find_next(distances, not_visited)
    return distances[ELEVATIONS == END][0]

# PART 1

ELEVATIONS = np.array([list(l) for l in lines])
s_row, s_col = get_position_elem(ELEVATIONS == START)
ELEVATIONS[ELEVATIONS == START] = REAL_START

part_1 = path_between_S_E(s_row, s_col)
print("PART 1:", int(part_1))

# PART 2

indices = zip(*np.where(ELEVATIONS == REAL_START))
min_distance = part_1
for coord in indices:
    row, col = coord
    if s_row != row or s_col != col:
        min_distance = min(min_distance, path_between_S_E(row, col))
print("PART 2:", int(min_distance))
