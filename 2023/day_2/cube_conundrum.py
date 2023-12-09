
import re

# from pprint import pprint as pp
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


def get_game_id(game: str) -> int:
    return int(game.removeprefix("Game ").split(':')[0])


def get_subsets(game: str) -> str:
    return game.split(':')[1]


def parse_subsets(subsets) -> tuple[list, list, list]:
    blue = re.compile(r"(\d*)\sblue")
    red = re.compile(r"(\d*)\sred")
    green = re.compile(r"(\d*)\sgreen")

    blue_matches = [int(i) for i in blue.findall(subsets)]
    red_matches = [int(i) for i in red.findall(subsets)]
    green_matches = [int(i) for i in green.findall(subsets)]

    return blue_matches, red_matches, green_matches


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
        (not any(red_cubes > total_red for red_cubes in red_matches))
        and (not any(blue_cubes > total_blue for blue_cubes in blue_matches))
        and (not any(green_cubes > total_green for green_cubes in green_matches))
        ):
        # print("valid game")
        game_id = get_game_id(game)
        # ic(game_id)
        return game_id
    return 0


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


# part_1()
part_2()
