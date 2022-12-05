from collections import deque
from pprint import pprint as pp
import re

from more_itertools import locate

datafiles = ["input.txt", "sample.txt", "sample_2.txt"]
datafile = datafiles[0]

with open(datafile, "r") as rf:
    lines = rf.readlines()

lines = [line.removesuffix("\n") for line in lines]


def get_number_of_stacks():
    for idx, line in enumerate(lines):
        if not line:
            return int(lines[idx - 1].split(" " * 3)[-1])


def get_max_stack_len():
    for idx, line in enumerate(lines):
        if not line:
            return idx - 1


def get_instructions():
    for idx, line in enumerate(lines):
        if not line:
            return lines[idx + 1 :]


def format_instructions(instructions):
    formatted_instructions = []
    regex = re.compile(r"^move\s(\d+)\sfrom\s(\d+)\sto\s(\d+)$")
    for instruction in instructions:
        result = re.search(regex, instruction)

        formatted_instruction = {
            "move": int(result.group(1)),
            "from": int(result.group(2)),
            "to": int(result.group(3)),
        }
        formatted_instructions.append(formatted_instruction)
    return formatted_instructions


def get_all_crates():
    for idx, line in enumerate(lines):
        if not line:
            return lines[: idx - 1]


def get_crate_indices(all_crates):
    all_crates_and_ids = []
    for crate in all_crates:
        indices = list(locate(crate, lambda x: x == "["))
        indices = [index + 1 for index in indices]
        indices = [round(index / 4) + (index % 4) for index in indices]
        crate_content = crate.replace(" ", "").replace("[", "").replace("]", "")
        crates_and_ids = {"crates": crate_content, "indices": indices}
        all_crates_and_ids.append(crates_and_ids)

    return all_crates_and_ids


def create_empty_stacks(number_of_stacks):
    return [deque() for _ in range(number_of_stacks)]


def place_crates_in_stacks(supply_stacks):
    for crates_and_ids in all_crates_and_ids[::-1]:
        for crate, index in zip(crates_and_ids["crates"], crates_and_ids["indices"]):
            index -= 1
            supply_stacks[index].append(crate)
    return supply_stacks


def move_crates_between_2_stacks(supply_stacks, instruction):

    move = instruction["move"]
    _from = instruction["from"]
    to = instruction["to"]

    # print(instruction)
    # print(move, _from, to)

    for _ in range(move):
        if not supply_stacks[_from - 1]:
            print(move, _from, to)
            print(supply_stacks[_from - 1])
            break
        crate_moved = supply_stacks[_from - 1].pop()
        # print(crate_moved)
        supply_stacks[to - 1].append(crate_moved)
        # print(supply_stacks[_from - 1], supply_stacks[to - 1])


def move_crates(supply_stacks, formatted_instructions):
    for instruction in formatted_instructions:
        for move, _from, to in zip(
            instruction["move"],
            instruction["from"],
            instruction["to"],
        ):
            move = int(move)
            _from = int(_from)
            to = int(to)
            # print(move, _from, to)
            for _ in range(move):
                if not supply_stacks[_from - 1]:
                    print(move, _from, to)
                    print(supply_stacks[_from - 1])
                    break
                crate_moved = supply_stacks[_from - 1].pop()
                # print(crate_moved)
                supply_stacks[to - 1].append(crate_moved)
                # print(supply_stacks[_from - 1], supply_stacks[to - 1])


def get_top_of_each_stack(supply_stacks):
    top_crates = ""
    for stack in supply_stacks:
        if stack:
            top_crates += stack[-1]
    return top_crates


number_of_stacks = get_number_of_stacks()
max_stack_len = get_max_stack_len()
instructions = get_instructions()
formatted_instructions = format_instructions(instructions)
all_crates = get_all_crates()
all_crates_and_ids = get_crate_indices(all_crates)
empty_stacks = create_empty_stacks(number_of_stacks)
supply_stacks = place_crates_in_stacks(empty_stacks)

# print(number_of_stacks)
# print(max_stack_len)
# pp(instructions)
# pp(formatted_instructions)
# for crate in all_crates:
#     print(crate)
# for crates_and_ids in all_crates_and_ids:
#     print(crates_and_ids)

# for supply_stack in supply_stacks:
#     print(supply_stack)

# instruction = formatted_instructions[0]
for instruction in formatted_instructions:
    # part 1
    move_crates_between_2_stacks(supply_stacks, instruction)
    # part 2

# move_crates(supply_stacks, formatted_instructions)
top_crates = get_top_of_each_stack(supply_stacks)
print(top_crates)
