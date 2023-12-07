
from pprint import pprint as pp

datafiles = ["input.txt", "input_sample.txt", "input_sample_2.txt"]
datafile = datafiles[-1]

with open(datafile, "r") as rf:
    lines = rf.readlines()

lines = [line.removesuffix("\n") for line in lines]

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
