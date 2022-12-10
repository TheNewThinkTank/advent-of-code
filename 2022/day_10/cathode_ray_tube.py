datafiles = ["input.txt", "sample.txt"]
datafile = datafiles[1]
with open(datafile, "r") as rf:
    lines = rf.readlines()
lines = [line.removesuffix("\n") for line in lines]

x = 1
cycle_no = 0


def get_signal_strength(x, cycle_no):
    return x * cycle_no


for line in lines:
    if line == "noop":
        cycle_no += 1
    else:
        instruction, v = line.split()
        print(instruction)
        print(v)
