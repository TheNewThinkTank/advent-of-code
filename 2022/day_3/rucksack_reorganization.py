# from pprint import pprint as pp
import string
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.get_data import get_data  # type: ignore

datafiles = ["input.txt", "sample.txt"]
datafile = datafiles[0]

lines = get_data(datafile)


def part_1():
    common_characters = ""
    for line in lines:
        # line = line.removesuffix("\n")
        assert len(line) % 2 == 0
        compartment_1 = line[: round(len(line) / 2)]
        compartment_2 = line[round(len(line) / 2) :]
        common_characters += "".join(set(compartment_1).intersection(compartment_2))
    return common_characters


priorities = {letter: i + 1 for i, letter in enumerate(string.ascii_letters)}

# pp(lines)
# pp(priorities)

# part 1
# common_characters = part_1()
# print(sum([priorities[letter] for letter in common_characters]))

# part 2
def divide_elves(lines: list, n: int):
    for i in range(0, len(lines), n):
        yield lines[i : i + n]


elf_groups = list(divide_elves(lines, 3))

common_characters = ""
for elf_group in elf_groups:
    # print(elf_group)
    common_characters += "".join(
        set(elf_group[0]).intersection(elf_group[1]).intersection(elf_group[2])
    )
# print(common_characters)
print(sum([priorities[letter] for letter in common_characters]))
