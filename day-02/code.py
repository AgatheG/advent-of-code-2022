from argparse import ArgumentParser
from enum import Enum

parser = ArgumentParser()
parser.add_argument(
    "-i", "-input", default="input.txt", dest="file")

args = parser.parse_args()

with open(args.file, "r") as file:
    strategy = file.read().split("\n")

class Moves(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

ALL_LEGIT_MOVE_VALUES = list(Moves)
GAIN = 3

def round_score(own_move, opponent_move):
    round_outcome = (own_move.value - opponent_move.value + 1) % len(ALL_LEGIT_MOVE_VALUES)
    return round_outcome * GAIN + own_move.value

OPPONENT_DECRYPTION_MAP = {
    "A": Moves.ROCK,
    "B": Moves.PAPER,
    "C": Moves.SCISSORS
}

OWN_DECRYPTION_MAP = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

# PART 1
total_score = 0
for round in strategy:
    encrypted_opponent_move, encrypted_own_move = round.split(" ")
    opponent_move = OPPONENT_DECRYPTION_MAP[encrypted_opponent_move]
    own_move = Moves(OWN_DECRYPTION_MAP[encrypted_own_move])
    total_score += round_score(own_move, opponent_move)
print(total_score)

# PART 2
def get_own_move(opponent_move, expected_outcome):
    idx_offset = expected_outcome - 2
    opponent_move_idx = ALL_LEGIT_MOVE_VALUES.index(opponent_move)
    own_move_idx = (opponent_move_idx + idx_offset) % len(ALL_LEGIT_MOVE_VALUES)
    return ALL_LEGIT_MOVE_VALUES[own_move_idx]

total_score = 0
for round in strategy:
    encrypted_opponent_move, encrypted_round_outcome = round.split(" ")
    opponent_move = OPPONENT_DECRYPTION_MAP[encrypted_opponent_move]
    expected_outcome = OWN_DECRYPTION_MAP[encrypted_round_outcome]
    own_move = get_own_move(opponent_move, expected_outcome)
    total_score += round_score(own_move, opponent_move)
print(total_score)
