from pathlib import Path

ROCK = 1
PAPER = 2
SCISSORS = 3

WINNING_MOVES = {
    ROCK: PAPER,
    PAPER: SCISSORS,
    SCISSORS: ROCK,
}
LOSING_MOVES = {val: key for key, val in WINNING_MOVES.items()}

INPUTS = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS,
}

def round_score(opponent, you):
    if opponent == you:
        return 3  # draw
    elif WINNING_MOVES[opponent] == you:
        return 6  # win
    else:
        return 0

score = 0
for line in Path("2.input").read_text().splitlines():
    opponent, you = [INPUTS[c] for c in line.split()]
    score += you + round_score(opponent, you)
print(score)

score = 0
for line in Path("2.input").read_text().splitlines():
    opponent_char, outcome = line.split()
    opponent = INPUTS[opponent_char]
    if outcome == "X":
        you = LOSING_MOVES[opponent]
    elif outcome == "Y":
        you = opponent
    else:
        you = WINNING_MOVES[opponent]
    score += you + round_score(opponent, you)
print(score)
