
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from src.get_data import get_data  # type: ignore
from src.get_full_path import get_full_path  # type: ignore
import numpy as np

datafiles = [
    "input.txt",
    ]
datafile = get_full_path("2024", "day_1", datafiles[0])
data = get_data(datafile)


def make_arrays():
    # left = np.array([3, 4, 2, 1, 3, 3])
    # right = np.array([4, 3, 5, 3, 9, 3])

    left = np.array([])
    right = np.array([])

    for d in data:
        dd = d.split()
        left = np.append(left, [int(dd[0])])
        right = np.append(right, [int(dd[1])])
    return left, right


def get_total_distance(left, right):
    # print(data)
    left.sort()
    right.sort()

    return np.abs(left-right).sum()


def get_similarity_score(left, right):

    unique, counts = np.unique(right, return_counts=True)
    _right = dict(zip(unique, counts))
    res = []
    for d in left:
        d = int(d)
        res.append(d * _right.get(d, 0))

    return sum(res)


left, right = make_arrays()
# print(get_total_distance(left, right))
print(get_similarity_score(left, right))
