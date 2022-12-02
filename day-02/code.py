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

def round_outcome(own_move, opponent_move):
    return (own_move - opponent_move + 1) % len(Moves)

GAIN = 3
OPPONENT_DECRYPTION_MAP = {
    "A": Moves.ROCK.value,
    "B": Moves.PAPER.value,
    "C": Moves.SCISSORS.value
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
    own_move = OWN_DECRYPTION_MAP[encrypted_own_move]
    total_score += own_move + round_outcome(own_move, opponent_move) * GAIN
print(total_score)

# PART 2
def get_own_move(opponent_move, expected_outcome):
    return (opponent_move + expected_outcome - 2) % len(Moves) + 1

total_score = 0
for round in strategy:
    encrypted_opponent_move, encrypted_round_outcome = round.split(" ")
    opponent_move = OPPONENT_DECRYPTION_MAP[encrypted_opponent_move]
    expected_outcome = OWN_DECRYPTION_MAP[encrypted_round_outcome]
    own_move = get_own_move(opponent_move, expected_outcome)
    total_score += own_move + round_outcome(own_move, opponent_move) * GAIN
print(total_score)
