from collections import defaultdict


datafiles = ["input.txt", "input_sample.txt"]
datafile = datafiles[0]


with open(datafile, "r") as rf:
    lines = rf.readlines()


def get_elfs_calories(lines):
    elfs_calories = defaultdict(list)
    elf_id = 1
    for line in lines:
        if line != "\n":
            line = int(line.removesuffix("\n"))
            elfs_calories[elf_id].append(line)
        else:
            elf_id += 1
    return elfs_calories


def get_elfs_calories_total(elfs_calories):
    elfs_calories_total = {}
    for k, v in elfs_calories.items():
        elfs_calories_total[k] = sum(v)
    return elfs_calories_total


elfs_calories = get_elfs_calories(lines)
elfs_calories_total = get_elfs_calories_total(elfs_calories)

sorted_elfs = sorted(elfs_calories_total.items(), key=lambda x: x[1], reverse=True)

# question 1
# print(sorted_elfs[0][1])

# question 2
calorie_total_top_3 = 0
for elf_id, calorie_total in sorted_elfs[0:3]:
    print(elf_id, calorie_total)
    calorie_total_top_3 += calorie_total
print(calorie_total_top_3)
