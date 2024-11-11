
# from pprint import pprint as pp
from icecream import ic
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.get_data import get_data  # type: ignore

datafiles = [
    "input.txt",
    "input_sample.txt",
    ]

datafile = datafiles[0]

lines = get_data(datafile)
# pp(lines)


def get_numbers(card: str):
    numbers = card.split(':')[1]
    numbers = [i.strip() for i in numbers.split('|')]
    winning_numbers = [int(i) for i in numbers[0].split(' ') if i]
    actual_numbers = [int(i) for i in numbers[1].split(' ') if i]

    return set(winning_numbers), set(actual_numbers)
    # return winning_numbers, actual_numbers


def get_num_wins(card: str):
    winning_numbers, actual_numbers = get_numbers(card)
    wins = winning_numbers.intersection(actual_numbers)
    return len(wins)


def part_1():
    total_points = 0
    for card in lines:
        num_wins = get_num_wins(card)
        # part 1
        points = 2 ** (num_wins - 1) if num_wins else 0
        total_points += points
        # ic(num_wins)
        # ic(points)
    ic(total_points)


# part 2


def get_card_id(card: str) -> int:
    return int(card.removeprefix("Card ").split(':')[0])


def init_cards_to_process():
    cards_to_process = {}  # card id and number of times it is due to be processed
    # before first iteration
    for card in lines:
        card_id = get_card_id(card)
        cards_to_process[card_id] = 1
    return cards_to_process


def update_cards_to_process(card):
    card_id = get_card_id(card)
    num_wins = get_num_wins(card)
    # ic(card_id)
    for _ in range(cards_to_process[card_id]):
        for win in range(card_id + 1, card_id + num_wins + 1):
            cards_to_process[win] += 1


# part_1()
cards_to_process = init_cards_to_process()
# ic(cards_to_process)
for card in lines:
    update_cards_to_process(card)
# ic(cards_to_process)
total_scratchcards = sum(cards_to_process.values())
ic(total_scratchcards)
