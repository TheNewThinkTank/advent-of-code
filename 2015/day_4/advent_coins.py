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


def starts_with_5_zeroes(secret_key: str, answer_candidate: str) -> bool:
    full_bstr = str.encode(secret_key + answer_candidate)
    md5_hash = hashlib.sha256(full_bstr).hexdigest()
    return md5_hash[:5] == "00000"


def get_lowest_positive_number(secret_key: str) -> int | None:
    for answer_candidate in range(1, 1_000_000):
        test = starts_with_5_zeroes(secret_key, str(answer_candidate))
        if test:
            return answer_candidate


tests = [
    {"input": "abcdef",
     "output": 609_043
     },
    {"input": "pqrstuv",
     "output": 1_048_970
     },
]

for test in tests:
    # assert get_lowest_positive_number(test["input"]) == test["output"]
    ic(get_lowest_positive_number(test["input"]))
    ic(test["output"])

# secret_key = "iwrupvqb"
# get_lowest_positive_number(secret_key)
