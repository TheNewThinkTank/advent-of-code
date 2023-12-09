
from pprint import pprint as pp
from icecream import ic

datafiles = [
    "input.txt",
    "input_sample.txt",
    ]

datafile = datafiles[0]

with open(datafile, "r") as rf:
    lines = rf.readlines()

lines = [line.removesuffix("\n") for line in lines]
# pp(lines)


def get_numbers(card: str):
    numbers = card.split(':')[1]
    numbers = [i.strip() for i in numbers.split('|')]
    winning_numbers = [int(i) for i in numbers[0].split(' ') if i]
    actual_numbers = [int(i) for i in numbers[1].split(' ') if i]

    return set(winning_numbers), set(actual_numbers)
    # return winning_numbers, actual_numbers


total_points = 0
for card in lines:
    winning_numbers, actual_numbers = get_numbers(card)
    wins = winning_numbers.intersection(actual_numbers)
    # wins = [i for i in actual_numbers if i in winning_numbers]
    num_wins = len(wins)

    # points = 2 * num_wins if num_wins > 2 else num_wins
    points = 2 ** (num_wins - 1) if num_wins else 0
    total_points += points

    # ic(num_wins)
    # ic(points)

ic(total_points)
