from pprint import pprint as pp

# from tqdm import tqdm
from icecream import ic

datafiles = [
    "input.txt",
    "input_sample_1.txt",
    "input_sample_2.txt",
    ]

datafile = datafiles[1]


def get_instructions_and_nodes():
    with open(datafile, "r") as rf:
        lines = rf.readlines()
    lines = [line.removesuffix("\n") for line in lines]
    lines = [line for line in lines if line]
    left_right_instructions = lines[0]
    elements = lines[1:]
    nodes_lr = {}
    for element in elements:
        first = element.partition(" = ")
        nodes_lr[first[0]] = first[2].strip("()").split(", ")
    return left_right_instructions, nodes_lr


left_right_instructions, nodes_lr = get_instructions_and_nodes()

ic(left_right_instructions)
ic(nodes_lr)

index_map = {"R": 1, "L": 0}

first_node = list(nodes_lr.keys())[0]
first_instruction = left_right_instructions[0]

ic(first_node)
ic(first_instruction)

ic(nodes_lr[first_node][index_map[first_instruction]])

# for instruction in left_right_instructions:
#     ic(instruction)
