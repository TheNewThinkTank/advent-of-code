datafiles = ["input.txt", "sample.txt"]
datafile = datafiles[0]

with open(datafile, "r") as rf:
    lines = rf.readlines()

line = lines[0].removesuffix("\n")


def get_marker_id(n):
    for idx, _ in enumerate(line):
        if idx < n - 1:
            continue
        if len(set(line[idx - n : idx])) == n:
            return idx


# part 1
start_of_packet = get_marker_id(4)
# print(start_of_packet)

# part 2
start_of_message = get_marker_id(14)
print(start_of_message)
