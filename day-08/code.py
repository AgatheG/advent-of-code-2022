from argparse import ArgumentParser
import numpy as np

parser = ArgumentParser()
parser.add_argument(
    "-i", "-input", default="input.txt", dest="file"
)

args = parser.parse_args()

with open(args.file, "r") as file:
    lines = file.read().split('\n')

NB_ROWS, NB_COLS = len(lines), len(lines[0])
TREE_HEIGHTS = np.zeros((NB_ROWS, NB_COLS))
for i in range(NB_ROWS):
    for j in range(NB_COLS):
        TREE_HEIGHTS[i, j] = lines[i][j]

# Count all exterior trees
visible_trees = 2 * NB_COLS + (2*NB_ROWS) - 4

for i in range(1, NB_ROWS - 1):
    for j in range(1, NB_COLS - 1):
        smaller_tree_than_current = (TREE_HEIGHTS - TREE_HEIGHTS[i, j]) < 0
        smaller_before_row, smaller_after_row = smaller_tree_than_current[i, 0 : j], smaller_tree_than_current[i, j + 1 : NB_COLS]
        smaller_before_col, smaller_after_col = smaller_tree_than_current[0 : i, j], smaller_tree_than_current[i + 1 : NB_ROWS, j]

        if smaller_before_row.all() or smaller_after_row.all() or smaller_before_col.all() or smaller_after_col.all():
            visible_trees += 1

print("Part 1: ", visible_trees)

L = []
for i in range(1, NB_ROWS - 1):
    for j in range(1, NB_COLS - 1):
        e, ee, eee, eeee = 0, 0, 0, 0
        x, xx, xxx, xxxx = True, True, True, True
        trees_higher_than_current_tree = TREE_HEIGHTS - TREE_HEIGHTS[i,j]
        trees_before_c = np.flip(trees_higher_than_current_tree[i,0:j])
        trees_after_c = trees_higher_than_current_tree[i,j+1:NB_COLS]
        trees_before_r = np.flip(trees_higher_than_current_tree[0:i,j])
        trees_after_r = trees_higher_than_current_tree[i+1:NB_ROWS,j]
        K = max(len(trees_before_c), len(trees_after_c), len(trees_before_r), len(trees_after_r))
        for k in range(K):
            if k < len(trees_before_c) and x:
                e += 1
                if trees_before_c[k] >= 0:
                    x = False
            if k < len(trees_after_c) and xx:
                ee += 1
                if trees_after_c[k] >= 0:
                    xx = False
            if k < len(trees_before_r) and xxx:
                eee += 1
                if trees_before_r[k] >= 0:
                    xxx = False
            if k < len(trees_after_r) and xxxx:
                eeee += 1
                if trees_after_r[k] >= 0:
                    xxxx = False
        L.append(e*ee*eee*eeee)
print(max(L))
                
