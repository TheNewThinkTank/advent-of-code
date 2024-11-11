"""
A nice string is one with all of the following properties:

It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
It contains at least one letter that appears twice in a row,
like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
It does not contain the strings ab, cd, pq, or xy,
even if they are part of one of the other requirements.
For example:

ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...),
a double letter (...dd...),
and none of the disallowed substrings.
aaa is nice because it has at least three vowels and a double letter,
even though the letters used by different rules overlap.
jchzalrnumimnmhp is naughty because it has no double letter.
haegwjzuvuyypxyu is naughty because it contains the string xy.
dvszwmarrgswjxmb is naughty because it contains only one vowel.
"""

import re
from icecream import ic

tests_part_1 = [
    {"input": "ugknbfddgicrmopn", "output": "nice"},
    {"input": "aaa", "output": "nice"},
    {"input": "jchzalrnumimnmhp", "output": "naughty"},
    {"input": "haegwjzuvuyypxyu", "output": "naughty"},
    {"input": "dvszwmarrgswjxmb", "output": "naughty"},
]

bad_strings = ["ab", "cd", "pq", "xy"]


def get_status_part_1(string):
    status = "nice"
    has_few_vowels = sum([string.count(x) for x in "aeiou"]) < 3
    if has_few_vowels:
        status = "naughty"

    if any(x in string for x in bad_strings):
        status = "naughty"

    pattern = re.compile(r'(\w)\1')
    match = re.search(pattern, string)
    if not match:
        status = "naughty"

    return status


for test in tests_part_1:
    assert get_status_part_1(test["input"]) == test["output"]

with open("input.txt", "r") as rf:
    strings = rf.readlines()
    strings = [d.strip("\n") for d in strings]

# ic(strings)
# part 2
"""
It contains a pair of any two letters,
that appears at least twice in the string without overlapping,
like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).

It contains at least one letter which repeats with exactly one letter between them,
like xyx, abcdefeghi (efe), or even aaa.

For example:
qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj)
and a letter that repeats with exactly one letter between them (zxz).
xxyxx is nice,
because it has a pair that appears twice and a letter that repeats with one between,
even though the letters used by each rule overlap.
uurcxstgmygtbstg is naughty,
because it has a pair (tg) but no repeat with a single letter between them.
ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo),
but no pair that appears twice.
"""

tests_part_2 = [
    {"input": "qjhvhtzxzqqjkmpb", "output": "nice"},
    {"input": "xxyxx", "output": "nice"},
    {"input": "uurcxstgmygtbstg", "output": "naughty"},
    {"input": "ieodomkazucvgmuy", "output": "naughty"},
]


def get_status_part_2(string):
    status = "nice"

    # positive lookahead assertion,
    # that checks for a pair of any two letters,
    # that appear at least twice without overlapping
    pair_pattern = re.compile(r'(?=(\w\w).*\1)')

    # checks for a letter that repeats with exactly one letter between them
    one_between_pattern = re.compile(r'(\w).\1')

    if not (
        bool(
            re.search(pair_pattern, string))
            and bool(re.search(one_between_pattern, string))
        ):
        status = "naughty"

    return status


for test in tests_part_2:
    assert get_status_part_2(test["input"]) == test["output"]


def count_nice_strings():
    nice_strings = 0
    for string in strings:
        status = get_status_part_2(string)  # get_status_part_1(string)
        if status == "nice":
            nice_strings += 1
    return nice_strings


nice_strings = count_nice_strings()
ic(nice_strings)
