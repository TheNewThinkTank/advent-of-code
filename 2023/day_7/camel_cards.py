
from pprint import pprint as pp
from collections import Counter
from operator import itemgetter

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
    {"hand": line.split(" ")[0],
     "bid": int(line.split(" ")[1])
    } for line in lines
]

# part 1
# pp(lines)
# ic(hands_and_bids)


def get_hand_type(hand):
    counts = Counter(hand)
    vals = sorted(list(counts.values()))
    hand_type = ""
    top_level_rank = 0
    if 5 in vals:
        hand_type = "Five of a kind"
        top_level_rank = 7
    elif 4 in vals:
        hand_type = "Four of a kind"
        top_level_rank = 6
    elif vals == [2, 3]:
        hand_type = "Full house"
        top_level_rank = 5
    elif vals == [1, 1, 3]:
        hand_type = "Three of a kind"
        top_level_rank = 4
    elif vals == [1, 2, 2]:
        hand_type = "Two pair"
        top_level_rank = 3
    elif vals == [1, 1, 1, 2]:
        hand_type = "One pair"
        top_level_rank = 2
    elif vals == [1, 1, 1, 1, 1]:
        hand_type = "High card"
        top_level_rank = 1

    return hand_type, top_level_rank


number_of_hands = len(hands_and_bids)

card_strengths = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1
}

for idx, hand_and_bid in enumerate(hands_and_bids):
    hand = hand_and_bid["hand"]
    bid = hand_and_bid["bid"]
    hand_type, top_level_rank = get_hand_type(hand)
    hands_and_bids[idx]["hand_type"] = hand_type
    hands_and_bids[idx]["top_level_rank"] = top_level_rank

hands_and_bids = sorted(hands_and_bids,
                        key=itemgetter('top_level_rank'),
                        reverse=True
                        )
# pp(hands_and_bids)


def second_ordering_rule(hand_and_bid1, hand_and_bid2):
    assert hand_and_bid1["top_level_rank"] == hand_and_bid2["top_level_rank"]
    # TODO: second ordering
    if card_strengths[hand_and_bid1["hand"][0]] > card_strengths[hand_and_bid2["hand"][0]]:
        print(hand_and_bid1["hand"] + " is stronger than " + hand_and_bid2["hand"])
    else:
        print(hand_and_bid1["hand"] + " is weaker than " + hand_and_bid2["hand"])
    # weakest hand gets rank 1


second_ordering_rule(hands_and_bids[0], hands_and_bids[1])
