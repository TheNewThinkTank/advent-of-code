
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.get_data import get_data  # type: ignore
from src.get_full_path import get_full_path  # type: ignore

datafiles = [
    "input.txt",
    "sample.txt",
    "sample_2.txt",
    "sample_3.txt",
    ]
datafile = get_full_path("2022", "day_10", datafiles[2])
lines = get_data(datafile)

x = 1
instruction_queue = []


def get_signal_strength(x, cycle_no):
    return x * cycle_no


print()
for idx, line in enumerate(lines):
    cycle_no = idx + 1

    print(f"start of cycle: {cycle_no}")
    print(f"{x = }, {line = }")

    if instruction_queue:
        # for k, v in instruction_queue[0].items():
        k, v = list(instruction_queue[0].items())[0]
        instruction_queue[0][k] -= 1
        if list(instruction_queue[0].values())[0] == 0:
            x += int(list(instruction_queue[0].keys())[0])
            instruction_queue.pop(0)

    if line == "noop":
        print(f"end of cycle: {cycle_no}")
        print(f"{x = }\n")
        continue

    _, v = line.split()
    cycles_to_wait = 2  # 1
    instruction_queue.append({v: cycles_to_wait})

    print(f"end of cycle: {cycle_no}")
    print(f"{x = }\n")

"""
while instruction_queue:

    cycle_no += 1
    print(f"start of cycle: {cycle_no}")
    print(f"{instruction_queue = }")
    print(f"{x = }")

    k, v = list(instruction_queue[0].items())[0]
    if list(instruction_queue[0].values())[0] == 0:
        x += int(list(instruction_queue[0].keys())[0])
        instruction_queue.pop(0)
    else:

        print(f"end of cycle: {cycle_no}")
        print(f"{x = }\n")

        cycle_no += 1
        instruction_queue[0][k] -= 1
        print(f"start of cycle: {cycle_no}")
        print(f"{instruction_queue = }")
        print(f"{x = }")

        if list(instruction_queue[0].values())[0] == 0:
            x += int(list(instruction_queue[0].keys())[0])
            instruction_queue.pop(0)
    print(f"end of cycle: {cycle_no}")
    print(f"{x = }\n")
"""
