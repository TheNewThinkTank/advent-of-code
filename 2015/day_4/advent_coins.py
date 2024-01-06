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


def starts_with_5_zeroes(secret_key, answer_candidate):
    full_bstr = str.encode(secret_key + answer_candidate)
    md5_hash = hashlib.sha256(full_bstr).hexdigest()
    return md5_hash[:5] == "00000"


secret_key = "iwrupvqb"
for answer_candidate in range(1, 1_000_000):
    test = starts_with_5_zeroes(secret_key, str(answer_candidate))
    if test:
        ic(answer_candidate)
        break
