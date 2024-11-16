
import re
# from pprint import pprint as pp
from icecream import ic
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.get_data import get_data  # type: ignore
from src.get_full_path import get_full_path  # type: ignore

datafiles = [
    "input.txt",
    "input_sample.txt",
    ]
datafile = get_full_path("2023", "day_2", datafiles[0])
lines = get_data(datafile)
# pp(lines)


def get_game_id(game: str) -> int:
    return int(game.removeprefix("Game ").split(':')[0])


def get_subsets(game: str) -> str:
    return game.split(':')[1]


def parse_subsets(subsets) -> tuple[list, list, list]:

    regex = lambda x: re.compile(fr"(\d*)\s{x}")
    matches = lambda x: [int(i) for i in x.findall(subsets)]

    return matches(regex("blue")), matches(regex("red")), matches(regex("green"))


# part 1


def filter_games(game: str,
                 blue_matches: list,
                 red_matches: list,
                 green_matches: list) -> int:

    # print(blue_matches)
    total_red = 12
    total_green = 13
    total_blue = 14

    if (
        any(red_cubes > total_red for red_cubes in red_matches)
        or any(blue_cubes > total_blue for blue_cubes in blue_matches)
        or any(green_cubes > total_green for green_cubes in green_matches)
        ):
        return 0
    return get_game_id(game)


def part_1() -> None:

    game_id_total = 0
    for game in lines:
        subsets = get_subsets(game)
        # ic(subsets)
        blue_matches, red_matches, green_matches = parse_subsets(subsets)
        game_id = filter_games(game, blue_matches, red_matches, green_matches)
        game_id_total += game_id
    ic(game_id_total)


def part_2() -> None:

    power_total = 0
    for game in lines:
        subsets = get_subsets(game)
        blue_matches, red_matches, green_matches = parse_subsets(subsets)
        power_total += max(blue_matches) * max(red_matches) * max(green_matches)
    ic(power_total)


part_1()
part_2()
