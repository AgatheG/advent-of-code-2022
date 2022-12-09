from argparse import ArgumentParser
import numpy as np

parser = ArgumentParser()
parser.add_argument(
    "-i", "-input", default="input.txt", dest="file"
)

args = parser.parse_args()

with open(args.file, "r") as file:
    lines = file.read().split('\n')

UP = "U"
DOWN = "D"
LEFT = "L"
RIGHT = "R"

def move_head(direction):
    if direction == UP:
        return (0, 1)
    if direction == DOWN:
        return (0, -1)
    if direction == LEFT:
        return (-1, 0)
    if direction == RIGHT:
        return (1, 0)

def move_tail(distance):
    if abs(distance[0]) > 1 and abs(distance[1]) > 1:
        coef_x, coef_y = -1*int(distance[0]/abs(distance[0])), -1*int(distance[1]/abs(distance[1]))
        return (distance[0] + coef_x, distance[1] + coef_y)
    if distance[0] < -1:
        return (distance[0] + 1, distance[1])
    if distance[0] > 1:
        return (distance[0] - 1, distance[1])
    if distance[1] > 1:
        return (distance[0], distance[1] - 1)
    if distance[1] < -1:
        return (distance[0], distance[1] + 1)
    return (0,0)

# PART 1
h_position = np.array([0,0])
t_position = np.array([0,0])
tail_distinct_positions = set()
for line in lines:
    direction, steps = line.split(" ")
    for i in range(int(steps)):
        h_position += move_head(direction)
        t_position += move_tail(h_position - t_position)
        tail_distinct_positions.add(str(t_position))
print("Part 1: ", len(tail_distinct_positions))

# PART 2
NB_KNOTS = 10
knot_positions = [np.array([0,0]) for i in range(NB_KNOTS)]
tail_distinct_positions = set()
for line in lines:
    direction, steps = line.split(" ")
    for i in range(int(steps)):
        for knot_idx in range(len(knot_positions) - 1):
            h_position, t_position = knot_positions[knot_idx], knot_positions[knot_idx + 1]
            if knot_idx == 0:
                h_position += move_head(direction)
            t_position += move_tail(h_position - t_position)
            if knot_idx + 1 == len(knot_positions) - 1:
                tail_distinct_positions.add(str(t_position))
print("Part 2: ", len(tail_distinct_positions))
