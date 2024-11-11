
import re
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.get_data import get_data  # type: ignore
from src.get_full_path import get_full_path  # type: ignore

datafiles = ["input.txt", "sample.txt"]
datafile = get_full_path("2022", "day_7", datafiles[0])
lines = get_data(datafile)

cd_dir_regex = re.compile(r"^\$\scd\s(.*)")
dir_regex = re.compile(r"^dir\s(.*)")
file_regex = re.compile(r"^(\d*)\s(.*)")

dir_names = []
abs_dir_paths_and_filesizes = {}

for line in lines:
    is_changing_dir = re.search(cd_dir_regex, line)
    dir_content = re.search(dir_regex, line)
    file_content = re.search(file_regex, line)

    if is_changing_dir:
        if is_changing_dir.group(1) == "..":
            dir_names.pop()
        else:
            dir_names.append(line.split()[2])

    elif file_content:
        for i in range(1, len(dir_names) + 1):
            abs_parent_dir = "/".join(dir_names[:i])
            if abs_parent_dir not in abs_dir_paths_and_filesizes:
                abs_dir_paths_and_filesizes[abs_parent_dir] = int(line.split()[0])
            else:
                abs_dir_paths_and_filesizes[abs_parent_dir] += int(line.split()[0])

# print(abs_dir_paths_and_filesizes)
small_dirs_sum = 0

total_disk_space = 70_000_000
needed_unused_space = 30_000_000
used_space = total_disk_space - abs_dir_paths_and_filesizes["/"]

deletion_size = needed_unused_space - used_space
large_dirs = []

for size in abs_dir_paths_and_filesizes.values():
    # part 1
    if size < 100_000:
        small_dirs_sum += size
    # part 2
    if size >= deletion_size:
        large_dirs.append(size)

# print(small_dirs_sum)

smallest_directory = min(large_dirs)
print(smallest_directory)
