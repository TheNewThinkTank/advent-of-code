
# from pprint import pprint as pp
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.get_data import get_data  # type: ignore
from src.get_full_path import get_full_path  # type: ignore

datafiles = [
    "input.txt",
    "input_sample.txt",
    "input_sample_2.txt",
    ]
datafile = get_full_path("2023", "day_1", datafiles[-1])
lines = get_data(datafile)

# pp(lines)

# part 1
# res = 0
# for line in lines:
#     digits = [elem for elem in line if elem.isdigit()]
#     res += int(digits[0] + digits[-1])

# print(res)

# part 2
word_num_map = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

res = 0
for line in lines:
    print("before: ", line)
    for k, v in word_num_map.items():
        line = line.replace(k, str(v))
    print("after: ", line)
    # digits = [elem for elem in line if elem.isdigit()]
    # res += int(digits[0] + digits[-1])

# print(res)
