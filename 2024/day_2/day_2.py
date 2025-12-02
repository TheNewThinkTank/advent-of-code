
reports = [
    [7, 6, 4, 2, 1,],
    [1, 2, 7, 8, 9,],
    [9, 7, 6, 2, 1,],
    [1, 3, 2, 4, 5,],
    [8, 6, 4, 4, 1,],
    [1, 3, 6, 7, 9,],
]

for report in reports:
    for level in report:
        ...

# pairwise_diff = [report[i + 1] - report[i] for i in range(len(report) - 1)]

######################################


def check_safety(a):
    # Compute differences using zip
    diffs = (b - a for a, b in zip(a, a[1:]))
    first_diff = next(diffs, None)  # Get the first difference

    if first_diff is None:  # Handle edge case of a single-element list
        return False

    # Check if all differences are positive and in range(1, 4)
    if 1 <= first_diff <= 3:
        return all(1 <= diff <= 3 for diff in diffs)

    # Check if all differences are negative and in range(-3, -1)
    if -3 <= first_diff <= -1:
        return all(-3 <= diff <= -1 for diff in diffs)

    return False

# Read and process input efficiently
with open("../input.txt", "r") as file:
    total = sum(
        1 for line in file 
        if check_safety([int(num) for num in line.split()])
    )

print(total)

