datafiles = ["input.txt", "sample.txt", "sample_2.txt"]
datafile = datafiles[1]
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
        x += instruction_queue.pop(0)

    if line == "noop":
        continue

    print(f"end of cycle: {cycle_no}")
    print(f"{x = }")

    _, v = line.split()
    instruction_queue.append(int(v))


while instruction_queue:
    cycle_no += 1
    print(f"start of cycle: {cycle_no}")
    print(f"{x = }")
    x += instruction_queue.pop(0)
    print(f"end of cycle: {cycle_no}")
    print(f"{x = }")
