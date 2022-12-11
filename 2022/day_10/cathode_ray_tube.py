datafiles = ["input.txt", "sample.txt", "sample_2.txt"]
datafile = datafiles[0]
with open(datafile, "r") as rf:
    lines = rf.readlines()
lines = [line.removesuffix("\n") for line in lines]

x = 1
instruction_queue = []


def get_signal_strength(x, cycle_no):
    return x * cycle_no


for idx, line in enumerate(lines):
    cycle_no = idx + 1

    print(f"start of cycle: {cycle_no}")
    print(f"{x = }, {line = }\n")

    if instruction_queue:
        for k, v in instruction_queue[0].items():
            instruction_queue[0][k] -= 1
        if list(instruction_queue[0].values())[0] == 0:
            x += int(list(instruction_queue[0].keys())[0])  # instruction_queue.pop(0)
            instruction_queue.pop(0)

    if line == "noop":
        print(f"end of cycle: {cycle_no}")
        print(f"{x = }")
        continue

    _, v = line.split()
    cycles_to_wait = 1
    instruction_queue.append({v: cycles_to_wait})
    # cycles_to_wait -= 1

    print(f"end of cycle: {cycle_no}")
    print(f"{x = }")

while instruction_queue:

    cycle_no += 1
    print(f"start of cycle: {cycle_no}")
    print(f"{x = }")

    for k, v in instruction_queue[0].items():
        instruction_queue[0][k] -= 1

        if list(instruction_queue[0].values())[0] == 0:
            x += int(list(instruction_queue[0].keys())[0])
            instruction_queue.pop(0)

    print(f"end of cycle: {cycle_no}")
    print(f"{x = }")
