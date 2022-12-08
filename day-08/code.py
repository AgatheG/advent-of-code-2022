from argparse import ArgumentParser
import numpy as np

parser = ArgumentParser()
parser.add_argument(
    "-i", "-input", default="input.txt", dest="file"
)

args = parser.parse_args()

with open(args.file, "r") as file:
    lines = file.read().split('\n')

# Parse as np array
NB_ROWS, NB_COLS = len(lines), len(lines[0])
TREE_HEIGHTS = np.zeros((NB_ROWS, NB_COLS))
for i in range(NB_ROWS):
    for j in range(NB_COLS):
        TREE_HEIGHTS[i, j] = lines[i][j]

# PART 1
# Count all edge trees as visible
visible_trees = 2 * NB_COLS + (2*NB_ROWS) - 4

# Count all visible interior trees
for i in range(1, NB_ROWS - 1):
    for j in range(1, NB_COLS - 1):
        smaller_trees_than_current = (TREE_HEIGHTS - TREE_HEIGHTS[i, j]) < 0
        visible = False
        visible = visible or smaller_trees_than_current[i, 0 : j].all()
        visible = visible or smaller_trees_than_current[i, j + 1 : NB_COLS].all()
        visible = visible or smaller_trees_than_current[0 : i, j].all()
        visible = visible or smaller_trees_than_current[i + 1 : NB_ROWS, j].all()

        visible_trees += int(visible)

print("Part 1: ", visible_trees)

# Part 2
higher_scenic_score = 0
for i in range(1, NB_ROWS - 1):
    for j in range(1, NB_COLS - 1):
        scenic_score = 1
        higher_trees_than_current = (TREE_HEIGHTS - TREE_HEIGHTS[i, j]) >= 0
        higher_before_row = np.flip(higher_trees_than_current[i, 0 : j])
        higher_after_row = higher_trees_than_current[i, j + 1 : NB_COLS]
        higher_before_col = np.flip(higher_trees_than_current[0 : i, j])
        higher_after_col = higher_trees_than_current[i + 1 : NB_ROWS, j]

        for height_list in [higher_before_row, higher_after_row, higher_before_col, higher_after_col]:
            idx_of_first_higher_tree = np.argwhere(height_list)
            if idx_of_first_higher_tree.size > 0:
                idx_of_first_higher_tree = idx_of_first_higher_tree[0][0]
            else:
                idx_of_first_higher_tree = len(height_list) - 1
            distance_to_higher_tree = idx_of_first_higher_tree + 1
            scenic_score *= distance_to_higher_tree
        higher_scenic_score = max(higher_scenic_score, scenic_score)

print("Part 2: ", higher_scenic_score)
