
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


def second_ordering_rule(hand_and_bid_1, hand_and_bid_2):
    """compare overall ranks for two hands with the same top_level_rank.
    """
    assert hand_and_bid_1["top_level_rank"] == hand_and_bid_2["top_level_rank"]
    # TODO: second ordering
    # weakest hand gets rank 1
    highest_ranked_card = 0

    for card_1, card_2 in zip(hand_and_bid_1["hand"], hand_and_bid_2["hand"]):
        if card_strengths[card_1] > card_strengths[card_2]:
            # print(card_1 + " is stronger than " + card_2)
            highest_ranked_card = 1
        elif card_strengths[card_1] < card_strengths[card_2]:
            # print(card_1 + " is weaker than " + card_2)
            highest_ranked_card = 2
        # else:
        #   print(card_1 + " and " + card_2 + " are the same")
        if highest_ranked_card != 0:
            return highest_ranked_card
    return highest_ranked_card


top_level_rank_counts = {}
# Count the occurrences of each top_level_rank value
for item in hands_and_bids:
    top_level_rank = item['top_level_rank']
    top_level_rank_counts[top_level_rank] = top_level_rank_counts.get(top_level_rank, 0) + 1

# Display the counts for each top_level_rank value
for top_level_rank, count in top_level_rank_counts.items():
    # print(f"Top Level Rank {top_level_rank}: {count} occurrences")
    ic(top_level_rank, count)

# TODO: use count instead of no_bottom_rank_cards
# bottom_rank = hands_and_bids[-1]["top_level_rank"]
# no_bottom_rank_cards = len([item for item in hands_and_bids if item['top_level_rank'] == bottom_rank])
lowest_rank, lowest_count = list(top_level_rank_counts.items())[-1]
ic(lowest_rank)
ic(lowest_count)

if lowest_count == 1:
    hands_and_bids[-1]["final_rank"] = 1
else:
    highest_ranked_card = second_ordering_rule(hands_and_bids[-1], hands_and_bids[-2])
    if highest_ranked_card == 1:
        hands_and_bids[-1]["final_rank"] = 1
    else:
        hands_and_bids[-2]["final_rank"] = 1

# ic(bottom_rank)
# ic(no_bottom_rank_cards)
# highest_ranked_card = second_ordering_rule(hands_and_bids[0], hands_and_bids[1])

# pp(hands_and_bids)
