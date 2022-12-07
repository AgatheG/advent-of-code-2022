from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
    "-i", "-input", default="input.txt", dest="file"
)

args = parser.parse_args()

with open(args.file, "r") as file:
    lines = file.read().split("\n")

class Repo(object):
    def __init__(self, parent):
        self.size = 0
        self.parent = parent

# PART 1
COMMAND_PREFIX = '$'
CHANGE_DIR = 'cd'
PARENT_DIR = '..'
DIR_KEYWORD = 'dir'

REPO_SIZE_UPPER_BOUND = 100000

current_repo, repos, dir_total_size = None, [], 0
for line in lines:
    line = line.split(" ")
    if line[0] == COMMAND_PREFIX:
        if line[1] == CHANGE_DIR:
            if line[2] == PARENT_DIR:
                # Going back to parent repo: no more files/child repo in this repo
                # Current size is total size
                child_repo_size = current_repo.size
                current_repo = current_repo.parent
                current_repo.size += child_repo_size
                if child_repo_size < REPO_SIZE_UPPER_BOUND:
                    dir_total_size += child_repo_size
            else:
                # Entering a new repo
                current_repo = Repo(current_repo)
                repos.append(current_repo)
    elif line [0] != DIR_KEYWORD:
        current_repo.size += int(line[0])

# Updating the impacted repo sizes after visiting last repo
repo = current_repo
while repo.parent is not None:
    repo.parent.size += repo.size
    repo = repo.parent

print("PART 1", dir_total_size)

# PART 2
TOTAL_SPACE = 70000000
REQUIRED_UNUSED_SPACE = 30000000
current_unused_space = TOTAL_SPACE - repos[0].size
file_size_to_delete = REQUIRED_UNUSED_SPACE - current_unused_space

big_enough_repos = [repo.size for repo in repos if repo.size >= file_size_to_delete]
big_enough_repos.sort()
print("PART 2", big_enough_repos[0])
