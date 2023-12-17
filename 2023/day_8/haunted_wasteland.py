# from pprint import pprint as pp
from icecream import ic

datafiles = [
    "input.txt",
    "input_sample_1.txt",
    "input_sample_2.txt",
    ]

datafile = datafiles[0]


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


def get_next_node(current_node, current_instruction):
    return nodes_lr[current_node][index_map[current_instruction]]


steps = 1
first_node = list(nodes_lr.keys())[0]
next_node = get_next_node(first_node, left_right_instructions[0])
ic(next_node)
left_right_instructions = left_right_instructions * 100_000

while next_node != "ZZZ":
    steps += 1
    next_node = get_next_node(next_node, left_right_instructions[steps - 1])
    ic(next_node)

ic(steps)
