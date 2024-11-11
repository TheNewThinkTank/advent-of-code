
# from pprint import pprint as pp
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.get_data import get_data  # type: ignore

datafiles = ["input.txt", "sample.txt"]
datafile = datafiles[0]

lines = get_data(datafile)


def get_section_ids(elf_pair: list):
    elf_pair = elf_pair.split(",")

    section_ids_1 = [int(i) for i in elf_pair[0].split("-")]
    section_ids_1 = list(range(section_ids_1[0], section_ids_1[1] + 1))

    section_ids_2 = [int(i) for i in elf_pair[1].split("-")]
    section_ids_2 = list(range(section_ids_2[0], section_ids_2[1] + 1))

    return section_ids_1, section_ids_2


def is_fully_contained(ids_1, ids_2):
    if (ids_1[0] in ids_2 and ids_1[-1] in ids_2) or (
        ids_2[0] in ids_1 and ids_2[-1] in ids_1
    ):
        return True
    return False


def is_overlapping(ids_1, ids_2):
    if set(ids_1).intersection(ids_2):
        return True
    return False


fully_contained_count = 0
for elf_pair in lines:
    section_ids_1, section_ids_2 = get_section_ids(elf_pair)

    # part 1
    # if is_fully_contained(section_ids_1, section_ids_2):
    #     fully_contained_count += 1

    # part 2
    if is_overlapping(section_ids_1, section_ids_2):
        fully_contained_count += 1

print(fully_contained_count)

# pp(lines)
