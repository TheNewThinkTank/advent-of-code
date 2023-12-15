"""
"""

# from pprint import pprint as pp
from collections import Counter

# from tqdm import tqdm
from icecream import ic

datafiles = [
    "input.txt",
    "input_sample.txt",
    ]

datafile = datafiles[1]

with open(datafile, "r") as rf:
    lines = rf.readlines()
lines = [line.removesuffix("\n") for line in lines]

hands_and_bids = [
    (line.split(" ")[0], int(line.split(" ")[1])) for line in lines
]

# part 1
# pp(lines)
# ic(hands_and_bids)


def get_hand_type(hand):
    # Five of a kind: AAAAA
    # Four of a kind: AA8AA
    # Full house: 23332
    # Three of a kind: TTT98
    # Two pair: 23432
    # One pair: A23A4
    # High card: 23456

    ic(Counter(hand))

    unique_cards = len(set(hand))
    hand_type = {
        1: "Five of a kind",
        2: "Four of a kind, or Full house",
        3: "Three of a kind, or Two pair",
        4: "One pair",
        5: "High card",
    }
    return hand_type[unique_cards]


for hand_and_bid in hands_and_bids:
    hand = hand_and_bid[0]
    # ic(hand_and_bid)
    ic(hand)
    # unique_cards = len(set(hand))
    # ic(unique_cards)
    hand_type = get_hand_type(hand)
    ic(hand_type)
