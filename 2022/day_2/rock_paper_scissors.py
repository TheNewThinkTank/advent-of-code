opponent_moves = {"A": "rock", "B": "paper", "C": "scissors"}
my_moves = {"X": "rock", "Y": "paper", "Z": "scissors"}

shape_score = {"rock": 1, "paper": 2, "scissors": 3}
outcome_score = {"lost": 0, "draw": 3, "win": 6}

rules = {
    "AZ": "lost",
    "CY": "lost",
    "BX": "lost",
    "AX": "draw",
    "BY": "draw",
    "CZ": "draw",
    "CX": "win",
    "AY": "win",
    "BZ": "win",
}

datafiles = ["strategy_guide.txt", "sample.txt"]
datafile = datafiles[0]

with open(datafile, "r") as rf:
    lines = rf.readlines()


def get_game_rounds():
    game_rounds = []
    for line in lines:
        game_rounds.append(line.removesuffix("\n").replace(" ", ""))
    return game_rounds


game_rounds = get_game_rounds()


def part_1():
    game_score = 0
    for game_round in game_rounds:
        my_move = game_round[1]
        round_result = rules.get(game_round, "wrong format")
        round_shape_score = shape_score[my_moves[my_move]]
        round_total_score = outcome_score[round_result] + round_shape_score
        game_score += round_total_score
    return game_score


# part 1
# print(part_1())

# part 2
my_outcomes = {"X": "lost", "Y": "draw", "Z": "win"}
my_moves = {"K": "rock", "L": "paper", "M": "scissors"}

rules = {
    "AM": "lost",
    "CL": "lost",
    "BK": "lost",
    "AK": "draw",
    "BL": "draw",
    "CM": "draw",
    "CK": "win",
    "AL": "win",
    "BM": "win",
}

game_score = 0
for game_round in game_rounds:
    my_outcome = my_outcomes[game_round[1]]
    for k, v in rules.items():
        if k[0] == game_round[0]:
            if v == my_outcome:
                my_move = k[1]

    round_shape_score = shape_score[my_moves[my_move]]
    round_outcome_score = outcome_score[my_outcome]
    round_total = round_shape_score + round_outcome_score
    game_score += round_total

print(game_score)
