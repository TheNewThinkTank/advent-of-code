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
    if line == "noop":
        # cycle_no += 1
        continue
    _, v = line.split()
    v = int(v)
    print(v)
    instruction_queue.append(v)
    x += instruction_queue.pop(0)
    print(f"{x = }")
