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

def distance_from_current_to_neighbour(elevation_gap, distance_to_current, revert):
    if revert:
        return distance_to_current + 1 if elevation_gap >= -1 else float("inf")
    return distance_to_current + 1 if elevation_gap <= 1 else float("inf")

def update_neighbours(current_row, current_col, distances, revert):
    indices = [
        [current_row - 1, current_col], [current_row + 1, current_col],
        [current_row, current_col - 1], [current_row, current_col + 1]
    ]
    for neighbour_row, neighbour_col in indices:
        if 0 <= neighbour_row < ELEVATIONS.shape[0] - 1 and 0 <= neighbour_col < ELEVATIONS.shape[1] - 1:
            gap = ELEVATIONS[neighbour_row, neighbour_col] - ELEVATIONS[current_row, current_col]
            new_distance = distance_from_current_to_neighbour(
                gap, distances[current_row, current_col], revert
            )
            distances[neighbour_row, neighbour_col] = min(
                new_distance, distances[neighbour_row, neighbour_col]
            )

def hill_climbing(row, col, revert=False):
    not_visited = np.ones(ELEVATIONS.shape, dtype="bool")
    distances = np.ones(ELEVATIONS.shape) * float("inf")

    distances[row, col] = 0
    next = [row, col]

    while next:
        row, col = next
        not_visited[row, col] = False
        update_neighbours(row, col, distances, revert)
        next = find_next(distances, not_visited)
    return distances

# PART 1
ELEVATIONS = np.array([list(l) for l in lines])
start_row, start_col = get_position_elem(ELEVATIONS == START)
ELEVATIONS[ELEVATIONS == START] = REAL_START

end_mask = ELEVATIONS == END
ELEVATIONS[end_mask] = REAL_END
ELEVATIONS = ELEVATIONS.view("int32")

part_1 = hill_climbing(start_row, start_col)
print("PART 1:", int(part_1[end_mask]))

# PART 2
ELEVATIONS = np.array([list(l) for l in lines])
start_row, start_col = get_position_elem(ELEVATIONS == END)
ELEVATIONS[ELEVATIONS == END] = REAL_END

ELEVATIONS[ELEVATIONS == START] = REAL_START
ELEVATIONS = ELEVATIONS.view("int32")

part_1 = hill_climbing(start_row, start_col, revert=True)
print("PART 2:", int(min(part_1[ELEVATIONS == ord(REAL_START)])))
