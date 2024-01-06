"""
Find MD5 hashes which, in hexadecimal,
start with at least five zeroes.
The input to the MD5 hash is some secret key (your puzzle input, given below)
followed by a number in decimal.
To mine AdventCoins, you must find Santa the lowest positive number
(no leading zeroes: 1, 2, 3, ...) that produces such a hash.

For example:

If your secret key is abcdef,
the answer is 609043,
because the MD5 hash of abcdef609043 starts with five zeroes (000001dbbfa...),
and it is the lowest such number to do so
"""

import hashlib
from icecream import ic


def get_lowest_positive_number(secret_key: str) -> int | None:
    for d in range(1, 10_000_000):
        md5_hash = hashlib.md5(str.encode(secret_key + str(d))).hexdigest()
        # part 1
        # if md5_hash[:5] == "00000":
        #     return d
        # part 2
        if md5_hash[:6] == "000000":
            return d


# part 1
# tests = [
#     {"input": "abcdef", "output": 609_043},
#     {"input": "pqrstuv", "output": 1_048_970},
# ]
# for test in tests:
#     assert get_lowest_positive_number(test["input"]) == test["output"]

secret_key = "iwrupvqb"
lowest_positive_number = get_lowest_positive_number(secret_key)
ic(lowest_positive_number)
