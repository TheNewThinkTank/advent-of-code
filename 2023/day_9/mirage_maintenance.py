
# from pprint import pprint as pp
from tqdm import tqdm
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
datafile = get_full_path("2023", "day_9", datafiles[0])
lines = get_data(datafile)


def get_history(lines):

    new_lines = []
    for line in lines:
        line = [int(i) for i in line.split(' ')]
        new_lines.append(line)
    return new_lines


def make_sequences(line, sequences):
    next_sequence = [line[i + 1] - line[i]
                     for i in range(len(line) - 1)
                     ]
    sequences.append(next_sequence)
    if not all(x == 0 for x in next_sequence):
        make_sequences(next_sequence, sequences)
    return next_sequence


def make_all_sequences():

    new_lines = get_history(lines)

    all_sequences = []
    for line in new_lines:
        sequences = [line]
        make_sequences(line, sequences)
        all_sequences.append(sequences)
    return all_sequences


def update_all_sequences(all_sequences: list) -> None:
    for seq in all_sequences:

        seq = list(reversed(seq))

        for idx, s in enumerate(seq):
            if idx == 0:
                s.append(0)
            else:
                s.append(s[-1] + seq[idx - 1][-1])


all_sequences = make_all_sequences()

# part 1
# update_all_sequences(all_sequences)
# extrapolated_sum = sum([
#     l[0][-1]
#     for l in tqdm(all_sequences)
# ])

# part 2


def update_all_sequences_part_2(all_sequences: list) -> None:
    for seq in all_sequences:
        seq = list(reversed(seq))
        for idx, s in enumerate(seq):
            if idx == 0:
                s.append(0)
            else:
                s.insert(0, s[0] + seq[idx - 1][0] * -1)


update_all_sequences_part_2(all_sequences)
extrapolated_sum = sum([
    seq[0][0]
    for seq in tqdm(all_sequences)
])
ic(extrapolated_sum)
